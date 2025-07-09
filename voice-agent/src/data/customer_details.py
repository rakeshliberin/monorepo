from dataclasses import dataclass
from typing import List
from markitdown import MarkItDown, StreamInfo
import requests
import httpx
import asyncio
from src.utils import logger


@dataclass
class BPData:
    """Value object to hold BP data from the SAP API response."""

    mobile_number: str
    partner_number: str
    first_name: str
    last_name: str
    street: str
    street_supplement: str
    house_number: str
    message: str = ""

    def summary(self) -> str:
        return (
            f"BP Number: {self.partner_number}\n"
            f"Name: {self.first_name} {self.last_name}\n"
            f"Address: {self.house_number}, {self.street}, {self.street_supplement}\n"
            "---\n"
        )


@dataclass
class BillingDetails:
    """Value object to hold billing details from the SAP API response."""

    bp_number: str
    due_date: str
    amount_due: float
    first_name: str
    last_name: str
    mobile_number: str
    bill_number: str
    bill_date: str

    def summary(self) -> str:
        return (
            f"BP Number: {self.bp_number}\n"
            f"Bill Number: {self.bill_number}\n"
            f"Bill Date: {self.bill_date}\n"
            f"Due Date: {self.due_date}\n"
            f"Amount Due: {self.amount_due}\n"
            f"Name: {self.first_name} {self.last_name}\n"
            f"Mobile Number: {self.mobile_number}\n"
            "---\n"
        )


@dataclass
class GetBPFromMobileResponse:
    """Value object to hold the response from the SAP API response."""

    status: str
    message: str
    last_name: str
    outstanding_details: str
    billing_information: str


async def get_bp_from_mobile(mobile_number: str) -> GetBPFromMobileResponse:
    """
    Get BP from mobile number

    Args:
        mobile_number (str): The mobile number to search for BP numbers

    Returns:
        tuple[str, str]: A tuple containing the BP numbers and associated details
    """

    try:
        # Check mobile number is does not contain +91
        if mobile_number.startswith("+91"):
            mobile_number = mobile_number[3:]

        # Check mobile number is does not contain 0
        if mobile_number.startswith("0"):
            mobile_number = mobile_number[1:]

        # Check mobile number is does not contain 91
        if mobile_number.startswith("91"):
            mobile_number = mobile_number[2:]

        url = f"https://webonline.igl.co.in:8077/sap/opu/odata/sap/ZCRM_FETCH_BP_FROM_MOBILE_SRV_01/BpSet?%24filter=ImMobileNo%20eq%20(%27{mobile_number}%27)&%24format=json"
        headers = {"Cookie": "sap-usercontext=sap-client=300"}

        resp = requests.get(url, headers=headers)
        resp.raise_for_status()

        logger.info(f"📥 Response Status: {resp.status_code}")
        logger.info(f"📥 Response Headers: {dict(resp.headers)}")

        if resp.status_code == 200:
            # Parse json to dataclass
            response = resp.json()["d"]
            logger.info(f"📥 Response: {response}")
            results = response["results"]
            logger.info(f"📥 Results: {results}")

            bp_list: List[BPData] = []

            for result in results:
                if result["Message"] == "":
                    bp_data = BPData(
                        mobile_number=result["ImMobileNo"],
                        partner_number=result["Partner"],
                        first_name=result["NameFirst"],
                        last_name=result["NameLast"],
                        street=result["Street"],
                        street_supplement=result["StrSuppl2"],
                        house_number=result["HouseNum1"],
                        message=result["Message"],
                    )
                    logger.info(f"📥 BP Data: {bp_data}")

                    bp_list.append(bp_data)

            if len(bp_list) == 0:
                logger.error(f"📥 No BP found for mobile number: {mobile_number}")
                return GetBPFromMobileResponse(
                    status="error",
                    message=f"No BP found for mobile number: {mobile_number}",
                    outstanding_details="",
                    billing_information="",
                )

            async with httpx.AsyncClient() as client:
                tasks = []
                bp_list_with_outstanding_details = ""
                bp_list_with_billing_information = ""

                for bp in bp_list:
                    logger.info(f"📥 Fetching customer details for {bp.partner_number}")
                    tasks.append(
                        asyncio.create_task(
                            fetch_customer_details(bp.partner_number, client)
                        )
                    )
                    tasks.append(
                        asyncio.create_task(
                            fetch_billing_information(bp.partner_number)
                        )
                    )

                results = await asyncio.gather(*tasks)
                logger.info(f"📥 Results: {results}")

                for i in range(len(results)):
                    if i % 2 == 0:
                        bp_list_with_outstanding_details += f"{results[i]}\n---\n"
                    else:
                        bp_list_with_billing_information += f"{results[i]}\n---\n"

            logger.info(f"📥 Customer details: {bp_list_with_outstanding_details}")
            logger.info(f"📥 Billing information: {bp_list_with_billing_information}")

            return GetBPFromMobileResponse(
                status="success",
                message="BP details fetched successfully",
                last_name=bp_list[0].last_name,
                outstanding_details=bp_list_with_outstanding_details,
                billing_information=bp_list_with_billing_information,
            )
        else:
            logger.error(f"📥 Response Error: {resp.text}")
            return GetBPFromMobileResponse(
                status="error",
                message=f"Failed to get BP from mobile number: {mobile_number}",
                last_name="",
                outstanding_details="",
                billing_information="",
            )
    except Exception as exc:
        logger.error(f"Customer‑details error: {exc}")
        return GetBPFromMobileResponse(
            status="error",
            message=f"Failed to get BP from mobile number: {mobile_number}",
            last_name="",
            outstanding_details="",
            billing_information="",
        )


async def fetch_customer_details(
    bp_number: str, client: httpx.AsyncClient = None
) -> str:
    url = f"https://webonline.igl.co.in:8077/sap/opu/odata/sap/Z_MONEY_N_MOBILE_SRV/money_n_mobileSet(Gpart='{bp_number}',ImVendorCode='IGLGUPCHAT')?$format=json"
    try:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()["d"]
        logger.info(f"📥 Customer details for {bp_number}: {data}")
        if data.get("Message") == "":
            billing_details = BillingDetails(
                bp_number=bp_number,
                amount_due=data.get("EtPostduedt", 0.0),
                due_date=data.get("EtDuedt", ""),
                first_name=data.get("NameFirst", ""),
                last_name=data.get("NameLast", ""),
                mobile_number=data.get("Mobile", ""),
                bill_number=data.get("ExOpbel", ""),
                bill_date=data.get("ExBldat", ""),
            )
            return billing_details.summary()
        else:
            return f"No billing details found for BP number: {bp_number}"

    except Exception as exc:
        logger.error(f"Customer‑details error: {exc}")
        return "Couldn't load account"


async def fetch_billing_information(bp_number: str) -> str:
    url = f"http://prdxecmapi.igl.co.in:8080/iglecmcustom/displayinvoice?bp_number={bp_number}&provider_id=QWERTYU003&provider_key=abapZ5qNXM"
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        md = MarkItDown()
        parsed = md.convert(resp, stream_info=StreamInfo(mimetype="application/pdf"))
        logger.info(f"Fetched last‑bill PDF for {bp_number}")
        return parsed.markdown
    except Exception as exc:
        logger.error(f"Billing‑PDF error: {exc}")
        return "Couldn't load bill"
