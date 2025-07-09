import json
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import FileResponse
import re
import os

PDF_DIR = './fake-server/pdf/'

app = FastAPI()


PDF_DATA = """
BUSINESS PARTNER N0. 4000569504

 NAME           :  Y SUBHASH
 ADDRESS      :  I-6/75
                         GRD FLOOR

                         POCKET 16
                         ROHINI SECTOR 16
                         NEW DELHI 110089

 MOBILE     :     9910308140
 EMAIL       :     y.subhash@igl.co.in

Current Bill Details          िबल िववरण

वतरमान

Bill Details(िबल िववरण)- Tax Invoice / Bill of Supply

 INVOICE NO.: 190002020077
चालान संखया :

Bill Date  : 24.02.2025

िबल की ितिथ :

 INVOICE TYPE: Retail
खुदरा
चालान पकार :
 CREDIT AMOUNT(If any)
के िडट रािश

 Amount Payable
 देय रािश
 After Due Date(2% LPC Applicable)
 देय ितिथ के बाद (2% एलपीसी लागू)
 Disconnection Date :
 (if bill not paid within Due Date)
 िवयोग ितिथ (यिद देय ितिथ के भीतर

 िबल का भुगतान नहंी िकया जाता है)

Due Date : 17.03.2025

 देय ितिथ   :
  ₹ 0

  ₹ 1635.11

  ₹ 1667.81

   01.04.2025

PART A (SALE OF NATURAL GAS)
भाग ए (पाकृ ितक गैस की िबकी)

1.1

1.2

1.3

Gas Consumption Charges

 गैस की खपत का शुलक

VAT VALUE वैट
Arrears: Unpaid dues up  to previous bill

िपछले िबल तक बकाया रािशा

1.4

Credit Balance:- Advance/Excess paid

के िडट बैलेस (जमा रािश)- अिगम/अितिरकत भुगतान
Adjustment for Estimated Bills समायोजन
Cheque Return Charges
Discount/Rebate छूट
Late Payment Charges

(₹)

1568.89

78.44

-12.22

0.00

TOTAL CHARGES (PART A)

कु ल शुलक

1635.11

PART - B (CHARGES) भाग बी
Fixed Daily Charges

िनधारिरत दैिनक शुलक

Other Service Charges

अनय सेवा शुलक

Minimum Charges

नयूनतम शुलक

TOTAL TAXABLE CHARGES

कु ल कर योगय शुलक

(₹)

SGST @ 9%

सटेट जीएसटी

CGST @ 9% सं

ैटर जीएसटी

Estimation Charges

TOTAL CHARGES (PART B)

कु ल शुलक

0

PART - C (SECURITY DEPOSIT) भाग सी
INSTALLATION/NORMAL SECURITY DEPOSIT PAYABLE

सुरका जमा देय
CONSUMPTIOIN SECURITY DEPOSIT PAYABLE
खपत सुरका जमा देय
EMI AMOUNT DUE  देय ईएमअाई रािश
Current EMI No

ईएमआई संखया

1.5

1.6

1.7

1.8

2.1

2.2

2.3

2.4

2.5

2.6

2.7

3.1

3.2

3.3

3.4

3.5

BILL DETAILS OF CONSUMPTION CYCLE

खपत चक का िबल िववरण

Meter No

मीटर संखया

Previous
Date

िपछली

तारीख

Closing Date

अंितम ितिथ

Previous
Meter
Reading

Closing
Meter
Reading

िपछली

वर्तमान

मीटर
रीिडंग

मीटर

रीिडंग

(₹)

ZEN00140
622/1218

21.12.2024

14.02.2025

882.570

916.470

TOTAL

No. of
days

िदनो की

संखया

56

56

UNITS
CONSUMED
(SCM)

खपत इकाइयो

की संखया

PRICE
PER UNIT

पित इकाई

GAS
CONSUMPTION
CHARGES(Exec
. VAT)

मूलय

गैस खपत शुलक

(वैट को छोड़कर)

33.900

46.28

1568.89

33.900

1568.89

Average Cons. in Last 2 billing cycles

अंितम २ िबिलंग चको मे औसत खपत

0.427 scm/day एससीेएम/िदन

Price/SCM in INR (w.e.f 09.04.2023)
मूलय/एससीएम

48.59  (incl. VAT) वैट सिहत

Additional Consumption SD

अितिरकत खपत सुरका जमा देय

Breakup Of Price /per SCM in INR                             (₹)

मूलय िववरण पित एससीएम

TOTAL CHARGES (PART C)

कु ल शुलक

TOTAL PAYABLE (A+B+C)

0

1635.11

कुल देय (ए+बी+सी)

Basic Cost of gas

Supply & Distribution cost

Margin

गैस की मूल लागत

आपूित और िवतरण लागत

26.72

15.14

मािजन

4.42

VAT

वैट

2.31

Total

कुल

48.59

कृपया ध्यान दे

01.10.2017 से वसतुओं और सेवाओं पर GST लागू है. हालाँिक GST कानून के  अनुसार PNG पर वैट लागू रहेगा

 >
ं की अगर द्िवमािसक गैस खपत की मात्रा ४ एससीएम से कम है, आपको न्यूनतम ४ एससीएम के िलए िबल भेजा जायेगा |
 > Kindly note that you will be billed for a minimum of 4 SCM, in case the bimonthly gas quantity is less than 4 SCM.
 >
 > GST is applicable on Goods & Services w.e.f. 01.10.2017. However, VAT will continue to be applicable on PNG Sales as per GST law
 >
 > Dear Customer, this is to inform you that Prices of PNG have been revised to Rs.48.59 per scm inclusive VAT w.e.f 09.04.2023
 > Note : Based on your past year consumption pattern ,we have revised your Consumption Security Deposit.The revised Additional Consumption
    Security Deposit(if any) will reflect in your next Bill

िपय गाहक, आपको सूिचत िकया जाता है िक 09.04.2023 से PNG की पभावी कीमते Rs.48.59 पित SCM वैट सिहत संशोिधत की गयी है।

> Dear Customer, Please save IGL’s WhatsApp No 9319850156. Text “ Hi ” and get in touch with IGL’s self-service options on WhatsApp to track your PNG bills and payments.

> Now pay your gas bills in cash at your nearest authorized *Common Services Center (CSC)* – Easy, Convenient, Secure! For complete list and address of CSC
outlets please visit IGL website.

9
4
3
8
1
0
4
4
0
0
0
0
0
0
0
0
P

TIN

CIN :

07200216284(w.e.f 5th April 1999)

Bill History

L23201DL1998PLC097614

Billing Period

Units (scm)

Cons/day (scm)

GSTN

07AAACI5076R1ZZ

19.10.2024-25.11.2024

26.11.2024-20.12.2024

14.340

12.570

0.377

0.503

(Authorised Signatory)

अिधकृ त हसताकरकतार

Please draw your cheque/DD favouring "INDRAPRASTHA GAS A/C Business Partner No. 4000569504"
DISCLAIMER : This bill is not a document for claiming any valid address proof of the PNG customer, for submitting before any Authority Body. Anybody claimimg or accepting the said
bill to be valid address proof shall be doing it at their own risk and cost.
"""


@app.get("/billing")
def get_pdf(bp_number: str = Query(..., min_length=10, max_length=10, regex=r"^\d{10}$")):
    # Validate input (should be exactly 10 digits)
    if not re.fullmatch(r"\d{10}", bp_number):
        raise HTTPException(
            status_code=400, detail="Input must be exactly 10 digits.")

    # pdf_path = os.path.join(PDF_DIR, f"{bp_number}.pdf")
    # if not os.path.isfile(pdf_path):
    #     raise HTTPException(
    #         status_code=404, detail="PDF not found for the given number.")

    return json.dumps({
        "bp_number": bp_number,
        "customer_details": "Y SUBHASH",
        "last_bill_text": PDF_DATA,
    })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
