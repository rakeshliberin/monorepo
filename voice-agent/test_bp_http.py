import requests
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import List

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

def test_bp_http(mobile_number: str):
    print(f"\n🔍 Testing BP HTTP call for mobile number: {mobile_number}")
    
    # API endpoint
    url = f"https://webonline.igl.co.in:8077/sap/opu/odata/sap/ZCRM_FETCH_BP_FROM_MOBILE_SRV_01/BpSet?%24filter=ImMobileNo%20eq%20(%27{mobile_number}%27)"
    headers = {"Cookie": "sap-usercontext=sap-client=300"}
    
    try:
        print("\n📡 Making HTTP request...")
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        
        print("\n📥 Response Status:", resp.status_code)
        print("📥 Response Headers:", dict(resp.headers))
        
        # Parse the XML response
        print("\n🔍 Parsing XML response...")
        print(resp.text)
        
        # Define namespaces
        namespaces = {
            'atom': 'http://www.w3.org/2005/Atom',
            'm': 'http://schemas.microsoft.com/ado/2007/08/dataservices/metadata',
            'd': 'http://schemas.microsoft.com/ado/2007/08/dataservices'
        }
        
        root = ET.fromstring(resp.text)
        
        # Extract BP data from XML
        bp_list = []
        for entry in root.findall('.//atom:entry', namespaces):
            properties = entry.find('.//m:properties', namespaces)
            if properties is not None:
                bp_data = BPData(
                    mobile_number=properties.find('.//d:ImMobileNo', namespaces).text,
                    partner_number=properties.find('.//d:Partner', namespaces).text,
                    first_name=properties.find('.//d:NameFirst', namespaces).text,
                    last_name=properties.find('.//d:NameLast', namespaces).text,
                    street=properties.find('.//d:Street', namespaces).text,
                    street_supplement=properties.find('.//d:StrSuppl2', namespaces).text,
                    house_number=properties.find('.//d:HouseNum1', namespaces).text,
                    message=properties.find('.//d:Message', namespaces).text or ""
                )
                bp_list.append(bp_data)
        
        if not bp_list:
            print("\n❌ No BP numbers found for the given mobile number.")
            return
        
        # Print results
        print("\n✅ Found BP numbers:")
        for bp in bp_list:
            print("\n📋 BP Details:")
            print(f"  BP Number: {bp.partner_number}")
            print(f"  Name: {bp.first_name} {bp.last_name}")
            print(f"  Address: {bp.house_number}, {bp.street}, {bp.street_supplement}")
            if bp.message:
                print(f"  Message: {bp.message}")
            print("  ---")
            
    except requests.exceptions.RequestException as e:
        print(f"\n❌ HTTP Error: {e}")
    except ET.ParseError as e:
        print(f"\n❌ XML Parse Error: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python test_bp_http.py <mobile_number>")
        print("Example: python test_bp_http.py 8750272155")
        sys.exit(1)
    
    mobile_number = sys.argv[1]
    test_bp_http(mobile_number) 