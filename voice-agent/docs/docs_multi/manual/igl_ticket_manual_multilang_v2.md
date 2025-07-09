---
title: "IGL Ticket Training Manual"
description: "Reference guide for AI Support Agent containing ticket categories, ticket handling procedures, TATs, and responsible departments for Indraprastha Gas Limited (IGL)."
source: "Indraprastha Gas Limited CRM Manual"
version: "1.0"
last_updated: "2025-05-10"
audience: "AI Support Agents, IGL Customer Service Representatives, Training Department"
keywords: "IGL, PNG, customer support, ticket handling, training, CRM, domestic gas, complaints, requests, emergency, TAT, standard operating procedures, SOP, Indraprastha Gas Limited"
chunking: "Each specific ticket type detailed under its own level-2 heading (##) forms an independent knowledge chunk. Overview tables and general procedure sections (e.g., Lead Creation) are also distinct chunks. The initial 'Ticket Overview' table is a key summary chunk."
multilingual_support: true
languages_supported: ["English", "Hindi", "Hinglish"]
---

# IGL Ticket Training Manual

## PNG Marketing
<!-- synonyms: PNG Marketing -->
### PNG CONNECTION DIAGRAM
## Ticket Overview
<!-- synonyms: Ticket Overview -->
This table summarizes domestic ticket categories, their Turnaround Times (TATs), and the concerned departments.

**Domestic Ticket Category**

| **S.No.** | **Ticket Type** | **TAT** | **Concern Department** |
| --------- | --------------------------------------- | ---------------- | ---------------------- |
|           | **DOM Query** |                  |                        |
| 1.        | Dom Query Service                       | 1 Day            | Call Center            |
| 2.        | Dom Query Understand Bill               | 1 Day            | Call Center            |
| 3.        | Dom Query Payment Options               | 1 Day            | Call Center            |
| 4.        | Dom Query Final Bill                    | 1 Day            | Call Center            |
|           | **DOM Emergency** |                  |                        |
| 1.        | No Gas Supply                           | 30 mins-03 hours | O&M                    |
| 2.        | Leakage                                 | 30 mins-03 hours | O&M                    |
|           | **DOM Requests** |                  |                        |
| 1.        | Temporary Disconnection -Renovation     | 13 Days          | O&M                    |
| 2.        | Temporary Disconnection-Personal Reason | 13 Days          | O&M                    |
| 3.        | Duplicate Bill                          | 4 Days           | Marketing              |
| 4.        | New Stove Conversion                    | 2 Days           | O&M                    |
| 5.        | NGC-NG Conversion                       | 3 Days           | Projects               |
| 6.        | Modification-GI                         | 11 Days          | O&M                    |
| 7.        | Modification PE                         | 9 Days           | O&M                    |
| 8.        | Permanent Disconnection                 | 7 Days           | O&M                    |
| 9.        | NACH Registration                       | 11 Days          | Marketing              |
| 10.       | E-Bill Registration                     | 1 Day            | Marketing              |
| 11.       | G/I DOM General Information             | 3 Days           | Call center            |
| 12.       | Reverse Late Payment Charges            | 6 Days           | Marketing              |
| 13.       | Retail Invoice Generation               | 10 Days          | Marketing              |
| 14.       | Rubber Tube Replacement                 | 2 Days           | O&M                    |
| 15.       | Refund                                  | 12 Days          | Marketing              |
| 16.       | Name and Address Correction             | 5 Days           | Marketing              |
| 17.       | Mod-Geyser/Extra-Point                  | 8 Days           | O&M                    |
| 18.       | Restoration With Device                 | 6 Days           | O&M                    |
| 19.       | Restoration Without Device              | 6 Days           | O&M                    |
| 20.       | Ownership Transfer                      | 14 Days          | Marketing              |
|           | **DOM Complaints** |                  |                        |
| 1.        | Wrong Meter Reading                     | 10 Days          | Marketing              |
| 2.        | High Billing                            | 30 Days          | Marketing              |
| 3.        | First Bill Not Generated                | 8 Days           | Marketing              |
| 4.        | D/EC-Delayed/Early connection           | 5 Days           | Projects               |
| 5.        | Flame Problem                           | 2 Days           | O&M, Projects          |
| 6.        | Incorrect Service Charges               | 7 Days           | Marketing              |
| 7.        | Re-measurement of Pipeline              | 10 Days          | O&M                    |
| 8.        | Defective Meter                         | 36 Days          | O&M                    |
| 9.        | Incorrect Meter Number                  | 10 Days          | O&M, Marketing         |
| 10.       | Billed Without Gas Supply               | 10 Days          | Marketing              |
| 11.       | Arrears In Billing                      | 8 Days           | Marketing              |
| 12.       | Improper Installation                   | 3 Days           | Projects, O&M          |

## Wrong Meter Reading
<!-- synonyms: Wrong Meter Reading | गलत मीटर रीडिंग | galat meter reading | wrong meter | meter reading error | मीटर रीडिंग गलती | गलत रीडिंग -->
This section details the 'Wrong Meter Reading' ticket, including when to raise it, TAT, and status reasons.

| **Category** | **Domestic Compliant** |
| ------------------ | ---------------------------------------------------------------------------------------- |
| **Ticket Type** | **Wrong Meter Reading** |
| **When** | **Meter reading on current retail bill is wrong as per customer VOC (Voice of Customer)** |
| **TAT** | **10 DAYS** |
| **Status Reasons** | **1.Meter Reading Correction Pending (Customer shared reading on call/email/ WhatsApp)**<br>**2.Meter Reading Collection Pending (Customer Wants Meter Reader Visit)** |

**Procedure:**
1.  Check Latest Bill Type in CRM (Estimated /Retail).
    * If Estimated: Raise RIG (Retail Invoice Generation).
    * If RETAIL BILL:
        * Ask customer for current reading on call & Check if Present reading shared is less/more than the Closing reading of the invoice.
        * **Reading Provided:**
            * Collect meter reading from the customer.
            * Verify Meter Number.
            * Enter Meter Reading/Meter Number provided.
            * Set status to: BO Pending (Meter Reading Correction).
            * Save and Inform TAT to customer (10 DAYS).
        * **Reading Not Shared:**
            * If customer not ready to share reading on call, offer submission on email/WhatsApp.
            * **Ready for email/WhatsApp:** Tag ticket under "Query Understand Bill" for email/WhatsApp team to create WMR ticket upon receiving reading.
            * **Not Ready to share at all:**
                * Set status to: BO Pending (Meter reading Collection).
                * Save and Inform TAT to customer (10 DAYS).

**Notes:**
1.  Suggest customer self-billing if due date of last bill is over and current reading is not shared over the call.
2.  If customer agrees to share reading over email/WhatsApp, tag ticket under "Query Understand Bill". The WMR ticket shall be created by email/WhatsApp team when reading is received after checking all details.
3.  Cases where bill raised on minimum consumption while customer had been actually using gas more than 4 scm, raise WMR.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/ email/ WhatsApp
* **Marketing:** meter reading updation
* **Finance:** Invoice generation
* **Ticket closure:** Marketing

## High Billing
<!-- synonyms: High Billing | अधिक बिलिंग | high billing | high bill | overbilling | ज्यादा बिल | अत्यधिक बिल -->
This section details 'High Billing' tickets, including triggers, TAT, and status reasons for bill disputes.

| **Category** | **Domestic Compliant** |
| ------------------ | --------------------------------------------------------- |
| **Ticket Type** | **High Billing** |
| **When** | **Bill is high / leakage adjustment as per customer VOC** |
| **TAT** | **30 DAYS** |
| **Status Reasons** | **Pending Bill Reversal** |

**Procedure:**
1.  If customer calls for High billing or Over Billing /Leakage adjustment.
2.  Check whether Bill is Estimated or Retail.
    * **Estimated Bill:** RIG (Retail Invoice Generation) to be raised.
    * **Retail Bill:**
        * Check CRM for previous TICKET FOR LEAKAGE/Defective meter.
            * If **Meter running fast and Meter found defective** OR **Leakage rectified from Downstream**: Raise High Billing Ticket - Back Office Pending Bill Reversal. Save & Inform The process. TAT- 30 DAYS.
            * If no such previous ticket:
                * Check Reading & Confirm.
                * **Reading not match:** Raise WMR (Wrong Meter Reading).
                * **Reading match:** Confirm Meter reading and Meter No. Check No of days, EMI/LPC, Arrear, Other charges and explain. If still disputed, raise Query UB (Understand Bill).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  In case of leakage or defective Meter adjustment, post rectification billing analysis is done approx. 15-20 days after rectification to understand consumption prior to leakage and post rectification. If same consumption pattern, no waiver.
2.  For adjustment amount less than Rs 500 no waiver is given. For cases where post analysis amount is greater than Rs 500, approval is raised and credit to the customer account after next 2 billing cycles (Approximately).
3.  Before meter leakage, no consideration. Rubber Tube also not considered. Downstream covers: appliance valve, copper pipe, GI pipe.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/ email
* **Control Room:** For leakage primary rectification, routing to marketing and reading collection.
* **Marketing:** Verify invoice, brief customer, update status (bill adjusted if no technical issue). Raise approval after billing analysis.
* **Ticket closure:** Marketing

## First Bill Not Generated
<!-- synonyms: First Bill Not Generated | पहला बिल नहीं बना | pehla bill | first bill not generated | no first bill | बिल नहीं बना | bill missing -->
This section covers 'First Bill Not Generated' (FBNG) tickets, including conditions, TAT, and related statuses.

| **Category** | **Domestic Compliant** |
| ------------------ | ----------------------------------------------------------------------------------- |
| **Ticket Type** | **First Bill Not generated** |
| **When** | **First bill not generated after 45-60 days of start of gas connection as per VOC** |
| **TAT** | **8 DAYS** |
| **Status Reasons** | 1. **BO Pending Invoice Not Generated** <br> 2. **Bo Pending Meter reading collection pending ( NG updated in CRM)** <br> 3. **BO Pending Move in Pending ( NG not updated in system)** |

**Procedure:**
1.  Check LEAD STATUS OF BP (Business Partner).
2.  JMR (Joint Meter Reading) DATE MENTIONED OR NOT?
    * **YES (JMR Date Mentioned):**
        * Request Customer to share Current Meter Reading.
        * **Reading Provided:**
            * Ask Meter Number & Match.
            * Verify Meter Number.
            * Enter Meter Number/Reading.
            * Status: BO Pending (Invoice not generated).
            * Save and Inform TAT (8 DAYS).
        * **Reading Not Provided:**
            * Status: BO Pending (Meter reading collection pending).
            * Save and Inform TAT (8 DAYS).
    * **NO (JMR Date Not Mentioned / JMR VERIFICATION PENDING):**
        * Status: BO Pending (Move in Pending).
        * Enter Meter Number & Save.
        * Save and Inform TAT (8 DAYS).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Ideally, bill should generate within 45-60 days of NG (Natural Gas connection). If customer calls before that and move-in is updated in CRM, request customer to wait. If more than 60 Days, raise FBNG.
2.  If customer can’t share reading over call, request meter pic on WhatsApp/email.
3.  Self-billing is not possible for FBNG.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email/WhatsApp
* **Marketing:** Move-in check and follow up with control room
* **O&M:** ticket status updating
* **Finance:** Invoice Generation
* **Ticket closure:** Finance

## Temporary Disconnection – Renovation
<!-- synonyms: Temporary Disconnection – Renovation | अस्थायी गैस कटौती - नवीनीकरण | temporary disconnection renovation | renovation disconnection | नवीनीकरण कटौती | मरम्मत के लिए गैस कट -->
This section details 'Temporary Disconnection - Renovation' requests, including device removal options, charges, and TAT.

| **Category** | **Dom Service Requests** |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| **Ticket Type** | **Temporary Disconnection- Renovation** |
| **When** | **Customer wants removal of Pipeline (with or without device) due to renovation** |
| **TAT** | **13 DAYS** |
| **Status Reasons** | **1.BO Pending With Device Removal (Customer wants removal of pipe + meter both due to renovation, construction work)** <br> **2.BO Pending Without Device Removal (Customer wants pipe removal only renovation, construction work)** |

**Procedure:**
1.  Customer asks for Pipe removal (with or without device) for construction or renovation.
2.  Confirm if Reinstallation of Pipe (GI) will take more than one day and if supply needs to be stopped for more than a day.
3.  Raise Temporary Disconnection Renovation ticket.
    * If **both meter & GI need to be removed**: Status: BO Pending (With Device Removal). Charges: 199/- visit charge + other charges confirmed by technician.
    * If **meter not to be removed, only GI pipe**: Status: BO Pending (Without Device Removal). Charges: 199/- visit charge + other charges confirmed by technician.
4.  Save and Inform TAT (13 DAYS).
5.  Bills locked after Temporary Disconnection until restoration; TD flag shown in CRM.

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  No bill generation until Restoration.
2.  Confirm supply stoppage timeline.
3.  Charges informed by technician based on pipe removed, length etc.
4.  Pipe in IGL custody; meter may be left with customer or taken by IGL.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email
* **O&M:** for execution of work at site
* **Marketing:** Billing Lock
* **Finance:** Customer Invoice
* **Ticket closure:** Marketing

## Temporary Disconnection- Personal Reason
<!-- synonyms: Temporary Disconnection- Personal Reason | अस्थायी गैस कटौती - व्यक्तिगत कारण | temporary disconnection personal | personal disconnection | व्यक्तिगत कारण कटौती | गैस बंद - निजी कारण -->
This section explains 'Temporary Disconnection - Personal Reason' (TDPR) requests, charges, and billing implications.

| **Category** | **Dom Service Requests** |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ticket Type** | **Temporary Disconnection- Personal Reason** |
| **When** | **Customer wants to stop gas supply for some time due to personal reason** |
| **TAT** | **13 DAYS** |
| **Status Reasons** | 1. **BO Pending Without Device Removal (Customer want to stop supply for personal reason e.g. going out of station/temporary moving out/going abroad & want billing lock.)** |

**Procedure:**
1.  Customer wants to stop supply temporarily for personal reason.
2.  Raise Temporary Disconnection Personal Reason ticket.
3.  Status: **BO Pending Without Device Removal**.
4.  Inform charges: Visit charge-199/-, Service Charges -168.27/-, and Rs.25 per month (after billing lock).
5.  Save. Billing Lock until restoration.
6.  Inform TAT (13 DAYS).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Billing lock until Restoration.
2.  Service charges of Rs 25/- per month levied and added in bill on restoration.
3.  Only Rubber tube disconnected and Appliance Valve closed.
4.  Suggest when customer is going out of station or won't use gas for a longer period.
5.  Service Charge for disconnection: Rs 168.27.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email
* **O&M:** for execution of work at site
* **Marketing:** Billing Lock
* **Finance:** Customer Invoice
* **Ticket closure:** Marketing

## Duplicate Bill
<!-- synonyms: Duplicate Bill | डुप्लीकेट बिल | bill copy | duplicate bill | बिल डुप्लीकेट | बिल प्रतिलिपि -->
This section covers requests for 'Duplicate Bills', both electronic and hard copy.

| **Category** | **Dom Service Requests** |
| ------------------ | ------------------------------------------------------------------------------------- |
| **Ticket Type** | **Duplicate Bill** |
| **When** | **Customer wants invoice copy or a duplicate bill or copy of the bill sent on email** |
| **TAT** | **4-7 DAYS (for hard copy)** |
| **Status Reasons** | 1. **BO Pending- Duplicate Bill Sent (Customer want invoice on mail id)** <br> 2. **BO Pending- Pending Hard Copy Dispatch (Customer want Hard Copy)** |

**Procedure:**
1.  Customer asks for Duplicate Bill.
    * **If Customer wants Bill on Mail:**
        * Confirm if Mail ID is registered.
        * If yes, send bill. If no, register Mail ID first & then send.
        * Status: BO Pending (Duplicate Bill Sent).
    * **IF Customer wants Hard Copy:**
        * Status: BO Pending (Pending Hard Copy Dispatch).
        * Inform TAT (4-7 working days).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Registered Mail ID mandatory for sharing invoice on mail.
2.  Hard copy bill takes 4-7 working days for delivery.
3.  Convince hardcopy customer for e-bill subscription and WhatsApp mode.

**Responsible Department:**
1.  **Call Center Operations:** for Ticket creation on call/email
2.  **Marketing and Vendor:** for Hard copy bill dispatch and closure.

## New Stove Conversion
<!-- synonyms: New Stove Conversion | नया स्टोव कन्वर्ज़न | new stove conversion | नया चूल्हा | stove conversion | चूल्हा परिवर्तन | gas stove install -->
This section outlines the 'New Stove Conversion' process for PNG compatibility.

| **Category** | **Dom Service Requests** |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Ticket Type** | **New Stove Conversion** |
| **When** | **Customer wants to change compatibility of Stove (LPG to PNG/ PNG to LPG) or bought a new stove which need to be made PNG compatible.** |
| **TAT** | **2 DAYS** |
| **Status Reasons** | 1. **BO Pending Request New Stove Conversion** |

**Procedure:**
1.  If Customer bought **a new stove needing PNG compatibility** OR complaints of No Gas Supply or Low Flame on connecting a new stove.
2.  Probe: Has Customer connected a New Stove or asking for Stove Conversion to PNG Compatible?
3.  If customer has connected new stove:
    * Raise New Stove Conversion ticket.
    * Status: BO Pending (Request New Stove Conversion).
    * Inform Service Charges: 63.11/- per Burner (No of Burner x 63.11/-).
    * Save and Inform TAT (2 DAYS).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  New Stove conversion is mostly for existing customers with a new stove.
2.  Check lead status to rule out NGC-NG conversion cases.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email
* **O&M:** for execution of work at site
* **Marketing:** inducing charges and ticket closure

## NGC-NG Conversion
<!-- synonyms: NGC-NG Conversion | एनजीसी से एनजी कन्वर्ज़न | ngc ng conversion | ngc to ng | conversion ngc | gas conversion -->
This section explains 'NGC-NG Conversion' (activating gas supply after meter installation).

| **Category** | **Dom Service Requests** |
| ------------------ | ------------------------------------------------------------------ |
| **Ticket Type** | **NGC- NG Conversion** (Natural Gas Connection to Natural Gas supply activation) |
| **When** | **Customer wants to activate gas supply after meter installation** |
| **TAT** | **3 DAYS** |
| **Status Reasons** | 1. **BO Pending Request (NG Conversion Requested)** |

**Procedure:**
1.  Customer asks to start Gas Supply after Meter Installation (after RFC - Ready For Connection).
2.  Check Lead Status ---RFC done/NG pending.
3.  Probe: Is TF (Termination Flange/Point) point connected?
    * **TF point connected (Gasified Area):**
        * Raise NG Conversion Ticket.
        * Status: BO Pending (NG Conversion Requested).
        * Inform TAT (3 DAYS).
        * Save and Inform TAT.
    * **TF point not connected (Non-Gasified Area):**
        * Tag in Internal note of Lead and fill Project and acquisition form.
        * Share timelines to customer for gasification. Do not raise NG Conversion ticket.

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Do not raise ticket before meter installation confirmed (RFC done).
2.  Probing for MDPE line/TF point connection, or nearby active supply is mandatory.
3.  Checking lead status is mandatory.
4.  For Non-gasified area, do not raise NG ticket. Share timelines.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email
* **Projects:** for execution of work at site
* **Marketing:** Ticket closure

## Modification-GI
<!-- synonyms: Modification-GI | जीआई पाइप संशोधन | modification gi | gi modification | जीआई बदलाव | gi pipe change | जस्ती पाइप संशोधन -->
This section details 'Modification-GI' requests for relocating GI pipelines or meters.

| **Category** | **Dom Service Requests** |
| ------------------ | --------------------------------------------------- |
| **Ticket Type** | **Modification- GI** (Galvanized Iron pipeline)     |
| **When** | **Customer wants to relocate GI pipeline or Meter** |
| **TAT** | **11 DAYS** |
| **Status Reasons** | 1. **BO Pending Requested Modification** |

**Procedure:**
1.  Customer wants Shifting/Rerouting of GI Pipeline (with or without Meter).
2.  Probe: Gas Supply stoppage needed? Or work completed same day?
3.  Raise Modification-GI ticket.
4.  Status: BO Pending (Requested Modification).
5.  Inform charges will be confirmed by technician.
6.  Save & Inform TAT (11 DAYS).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Gas supply continues after Modification work (unless extensive work requires temporary stoppage by O&M).
2.  Only for GI pipe or Meter shifting. For TF or MDPE line shifting, raise Modification- PE ticket.
3.  No Billing lock in Modification- GI.
4.  If customer calls for restoration, no TDR in CRM, and GI pipe work needed, Modification GI ticket might be raised.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email
* **O&M:** for execution of work at site
* **Marketing:** inducing charges and Ticket closure

## Modification PE
<!-- synonyms: Modification PE | पीई पाइप संशोधन | modification pe | pe modification | पीई बदलाव | pe pipe change | पॉलीइथिलीन पाइप संशोधन -->
This section covers 'Modification-PE' requests for shifting TF points or MDPE lines.

| **Category** | **Dom Service Requests** |
| ------------------ | ------------------------------------------------- |
| **Ticket Type** | **Modification- PE** (Polyethylene pipeline)      |
| **When** | **Customer wants to shift TF point or MDPE line** |
| **TAT** | **9 DAYS** |
| **Status Reasons** | 1. **BO Pending Requested Modification** |

**Procedure:**
1.  Customer wants to change TF Point or MDPE line.
2.  Probe: User or Non-User?
3.  Raise Modification- PE ticket.
4.  Collect Address, contact no., mail id.
5.  Status: BO Pending Requested Modification.
6.  Inform 199/- visit charges + other charges confirmed by technician.
7.  Forward details to respective Control Room if necessary.
8.  Save & Inform TAT (9 DAYS).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Only for TF point or MDPE line shifting. For GI pipe/meter shifting, raise [Modification-GI](#modification-gi).
2.  Charges confirmed by technician, added to bill for users.
3.  Non-user modification typically not charged to an individual.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email.
* **O&M (or Projects for larger scale PE work):** for execution of work at site.
* **Marketing:** inducing charges (for users) and Ticket closure.

## Permanent Disconnection
<!-- synonyms: Permanent Disconnection | स्थायी गैस कटौती | permanent disconnection | permanent cutoff | स्थायी कटौती | gas cancellation | गैस सेवा बंद -->
This section explains 'Permanent Disconnection' of gas service for private and government connections.

| **Category** | **Dom Service Requests** |
| ------------------ | ------------------------------------------------------- |
| **Ticket Type** | **Permanent Disconnection** |
| **When** | **Customer wants to disconnect connection permanently** |
| **TAT** | **7 DAYS** |
| **Status Reasons** | 1. **BO Pending (With Device Removal)** <br> 2. **BO Pending (Without Device Removal)** |

**Procedure:**
1.  Customer asks for Permanent Disconnection.
2.  Determine connection type:
    * **Government Connection:** Raise **Temporary Disconnection- Personal Reason** ticket. Status: BO Pending without Device Removal (under TDPR). Charges: 199/- + 168.27/- + 25 Rs/month (TDPR charges). TAT: 13 Days (for TDPR).
    * **Private Connection:** Raise Permanent Disconnection Ticket. Status: BO Pending with Device Removal. Charges: 199/- visit charge + technician confirmed service charges (approx. 183 Rs/-). TAT (7 DAYS).
3.  After PD, material in IGL custody.

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Government body connections generally not permanently disconnected; use TDPR.
2.  NOC generally not provided for Private PD or TDPR unless specific regulatory needs exist.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email
* **O&M:** for execution of work at site
* **Marketing:** inducing charges, final bill processing, Ticket closure

## D/EC- Delayed/ Early connection
<!-- synonyms: D/EC- Delayed/ Early connection | कनेक्शन में देरी / जल्दी | delayed early connection | late connection | early connection | delayed connection | समय से पहले कनेक्शन | कनेक्शन में देरी -->
This section describes handling of 'Delayed/Early Connection' (D/EC) requests for meter installation.

| **Category** | **Dom Complaints** |
| ------------------ | ----------------------------------------------------------------------------------------- |
| **Ticket Type** | **D/EC- Delayed/ Early Connection** |
| **When** | **Customer wants meter installation before TAT or TAT is over & installation is pending** |
| **TAT** | **5 DAYS** (for resolution of D/EC ticket) |
| **Status Reasons** | 1. **D/EC- Back Office Pending RFC (Ready For Connection)** |

**Procedure:**
1.  Customer asks for Meter Installation.
2.  Check if CA (Customer Acquisition/Connection Agreement) generated OR if 90 days over from CA generation.
    * **Builder Connection (KYC pending):** Guide for Builder KYC. Do not raise D/EC ticket.
    * **90 days over after CA generation (Delayed):** Raise D/EC-Delayed/Early connection ticket.
    * **After CA, customer insists for early installation (Early Request):** Raise D/EC-Delayed/Early connection ticket.
3.  Status for ticket: D/EC-Back Office Pending RFC.
4.  Inform TAT for D/EC ticket processing: 5 Days.

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  **Delayed:** If 90 days over post-CA and meter not installed, raise D/EC to expedite.
2.  **Early Request:** Ask customer to wait normal TAT. If insists, raise D/EC for possible expedition.
3.  **Company/Builder Name Holder:** Guide for Builder KYC for NG activation.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email
* **Projects:** for execution of work at site
* **Marketing:** Coordination and Ticket closure (of D/EC ticket)

## Flame Problem
<!-- synonyms: Flame Problem | फ्लेम समस्या | low flame | flame problem | कम आंच | flame low | flame issue | आंच समस्या | yellow flame -->
This section details how to address 'Flame Problems' with PNG stoves.

| **Category** | **Dom Complaints** |
| ------------------ | -------------------------------------------------------- |
| **Ticket Type** | **Flame Problem** |
| **When** | **Customer is facing Flame problem (Low or high flame)** |
| **TAT** | **2 DAYS** |
| **Status Reasons** | 1. **BO Pending (Verify Flame Problem)** |

**Procedure:**
1.  Customer has Flame Problem (Low/High Flame/Burner Issue).
2.  Verify if customer bought/connected a New Stove.
    * **New Stove:** Tag request under New Stove Conversion ticket.
    * **Existing PNG stove:**
        * Raise Flame Problem ticket.
        * Status: BO Pending (Verify Flame Problem).
        * Inform Service Charges:
            * **Free:** within 15 days of first NG conversion & New Stove Conversion.
            * **Chargeable:** Visit charge: 199/- + Rs. 106.08/- per burner (After 15 days).
        * Inform TAT (2 DAYS).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  IGL addresses flame problems related to PNG supply/initial conversion, not general stove servicing.
2.  Probe if new stove connected or issue with same PNG stove.
3.  Low flame might indicate No Gas Supply in area (check wider outages).

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email
* **Projects or O&M:** for execution of work at site
* **Marketing:** Inducing charges (if applicable) and Ticket closure

## NACH Registration
<!-- synonyms: NACH Registration | नैच रजिस्ट्रेशन | nach registration | nach mandate | नैच मेनडेट | direct debit | ऑटो डेबिट -->
This section covers 'NACH Registration' for automatic bill payments.

| **Category** | **Dom Service Requests** |
| ------------------ | ------------------------------------------------------------------------------------- |
| **Ticket Type** | **NACH Registration** (National Automated Clearing House for auto-debit)             |
| **When** | **Customer wants auto-deduction for outstanding amount from IGL end.** |
| **TAT** | **11 DAYS** (for registration processing)                                         |
| **Status Reasons** | 1. **NACH BO Pending- Hard Copy Requested** <br> 2. **NACH BO Pending- Soft Copy Requested** |

**Procedure:**
1.  Customer wants to activate NACH services.
2.  Raise NACH Registration ticket.
    * If **Hard Copy** of NACH mandate form process: Status: NACH BO Pending- Hard Copy Requested.
    * If **Soft Copy** (e-mandate/scanned form) process: Status: NACH BO Pending- Soft Copy Requested.
3.  Inform TAT (11 Days).

**CRM Tagging/ Ticket Creation**

**Note:**
If bill amount exceeds registered NACH limit, auto-debit fails for that cycle.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email/whatsapp
* **PNG Marketing:** Process coordination
* **Marketing Team:** NACH setup and confirmation
* **Vendor (Banking partner/aggregator):** Technical processing
* **Ticket Closure:** Marketing Team

## Defaulter Restoration
<!-- synonyms: Defaulter Restoration | डिफॉल्टर रिस्टोरेशन | defaulter restoration | reconnect defaulter | डिफॉल्टर पुनः कनेक्शन | arrears restoration -->
This section explains the 'Defaulter Restoration' process for connections disconnected due to non-payment.

| **Category** | **Dom Complaints/Requests** |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| **Ticket Type** | **Defaulter Restoration** |
| **When** | **Customer wants restoration of connection disconnected due to non-payment.** |
| **TAT** | **6 DAYS** (after payment confirmation and ticket logging)                                                           |
| **Status Reasons** | 1. **BO Pending (Requested Restoration by Customer)** |

**Procedure:**
1.  Customer asks for Defaulter Restoration.
2.  Check CRM for Defaulter Disconnection ticket and Defaulter Flag.
3.  If connection confirmed disconnected for Default:
    * Confirm with customer: penalty of RS.3000/- paid + all outstanding cleared.
    * Customer provides payment proof.
    * Once payment verified:
        * Raise Defaulter Restoration ticket.
        * Status: BO Pending (Requested Restoration by Customer).
        * Inform TAT (6 Days).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  If no defaulter disconnection ticket in CRM, but customer dismantled pipes/supply stopped for other reasons mistaken for defaulter disconnection, and dues exist: different process may apply (e.g. Modification-GI). Rs.3000/- penalty specific to official defaulter disconnection.
2.  Customer pays Rs 3000 penalty + outstanding for restoration. Payment proof required.
3.  For DF flag status, no maintenance charges typically levied during disconnection.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation (after payment confirmation)
* **O&M:** for execution of work at site
* **Marketing Team:** Verifying payments, applying charges, ticket closure
* **Finance Team:** Confirming payment receipt

## E-Bill Registration
<!-- synonyms: E-Bill Registration | ई-बिल रजिस्ट्रेशन | e bill registration | ई बिल | online bill | इलेक्ट्रॉनिक बिल -->
This section details 'E-Bill Registration' for subscribing to or unsubscribing from electronic billing.

| **Category** | **Dom Service Requests** |
| ------------------ | ---------------------------------------------------------------------- |
| **Ticket Type** | **E-bill Registration** |
| **When** | **Customer wants to subscribe or unsubscribe for E-bill services** |
| **TAT** | **1 DAY** |
| **Status Reasons** | 1. **E-Bill Registered (Customer subscribes)** <br> 2. **E-Bill Deregistered (Customer unsubscribes)** |

**Procedure:**
1.  Customer wants bill on email (subscribe) or remove e-bill (unsubscribe).
2.  Check if customer's e-mail ID registered in CRM.
    * **Not registered (and wants to subscribe):** Update customer e-mail ID first.
3.  Raise E-Bill Registration ticket.
    * **To subscribe:** Status: E-Bill Registered.
    * **To unsubscribe:** Status: E-Bill Deregistered.
4.  Inform TAT (1 Day).

**CRM Tagging/ Ticket Creation**

**Note:**
1.  Rs.20 charged for hard copy. Guide customers to e-bill to avoid charges and save environment.
2.  E-bill registered tickets often auto-close. Deregistration may need manual processing.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation on call/email
* **Marketing:** Processing (especially deregistration) and Ticket closure

## G/I DOM General Information
<!-- synonyms: G/I DOM General Information | सामान्य जानकारी | general information | general info | सामान्य प्रश्न | query | dom query -->
This section describes 'G/I DOM General Information' tickets for queries not fitting specific categories.

| **Category** | **Dom Service Requests** |
| ------------------ | ------------------------------------------------------------------------------------ |
| **Ticket Type** | **G/I DOM General Information** (General Inquiry - Domestic)                           |
| **When** | **Customer has query and raises ticket from Chat bot, Connect App, website.** Or for queries not fitting other categories. |
| **TAT** | **3 DAYS** |
| **Status Reasons** | 1. **G/I- BO Pending General Info** |

**Procedure:**
1.  Ticket typically auto-created (Chatbot, App, Website) or by agent for uncategorized queries.
2.  Status Reason: G/I – BO Pending General Info.
3.  Inform TAT (3 Days) for call center team to address and close.

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  If customer calls with request/complaint not fitting existing CRM category, G/I ticket can be raised to allow time for resolution.
2.  Designated call center team to outcall customer, resolve, and close ticket.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation
* **Call center (Designated Team):** For outcall, resolution, and Ticket closure

## Incorrect Service Charges
<!-- synonyms: Incorrect Service Charges | गलत सेवा शुल्क | incorrect service charges | wrong service charge | service charge error -->
This section details handling of complaints regarding 'Incorrect Service Charges' on bills.

| **Category** | **Dom Complaints** |
| ------------------ | ------------------------------------------------------------------------------------------------------ |
| **Ticket Type** | **Incorrect Service Charges** |
| **When** | **Customer claims wrong services charges levied in bill /other charges head in bill** |
| **TAT** | **7 DAYS** |
| **Status Reasons** | 1. **BO Pending (Verify Incorrect Charges)** |

**Procedure:**
1.  Customer complains of Incorrect Service Charges in bill.
2.  Verify charges/services availed via past service tickets and job sheets.
3.  If discrepancy suspected or backend clarification needed:
    * Raise Incorrect Service Charges ticket.
    * Status: BO Pending (Verify Incorrect Charges).
    * Inform TAT (7 DAYS).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Check services taken and verify charges with JOBSHEET in service ticket.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation
* **Marketing & Finance:** Verification, rectification if needed, Ticket closure

## Re-measurement of Pipeline
<!-- synonyms: Re-measurement of Pipeline | पाइपलाइन का पुनः मापन | re measurement | pipeline remeasure | पाइपलाइन माप | पुनः माप -->
This section covers requests for 'Re-measurement of Pipeline'.

| **Category** | **Dom Complaints** |
| ------------------ | -------------------------------------------------- |
| **Ticket Type** | **Re-measurement of Pipeline** |
| **When** | **Customer wants re-measurement of pipeline** |
| **TAT** | **10 DAYS** |
| **Status Reasons** | 1. **BO Pending (Pending Pipe Re-measurement)** |

**Procedure:**
1.  Customer requests Pipeline Re-Measurement.
2.  Probe reason (e.g., disputes initial measurement, billing issues).
3.  Raise Re-measurement of Pipeline ticket.
4.  Status: BO Pending (Pending Pipe Re-measurement).
5.  Inform TAT (10 DAYS).

**CRM Tagging/ Ticket Creation**

**Responsible Department:**
* **Call Center Operations:** for Ticket creation
* **O&M (site visit & measurement) & Marketing (billing adjustment if any):** Ticket closure (Marketing after O&M input)

## Reverse Late Payment Charges
<!-- synonyms: Reverse Late Payment Charges | लेट पेमेंट चार्ज रिवर्सल | reverse late payment charges | late fee reversal | लेट फीस रिवर्स | एलपीसी रिवर्स -->
This section details requests for 'Reverse Late Payment Charges' (LPC).

| **Category** | **Dom Service Requests** |
| ------------------ | --------------------------------------------------- |
| **Ticket Type** | **Reverse Late Payment Charges (LPC)** |
| **When** | **Customer wants reversal of Late Payment Charges** |
| **TAT** | **6 DAYS** |
| **Status Reasons** | 1. **BO Pending (Verify LPC)** |

**Procedure:**
1.  Customer asks for LPC reversal.
2.  Verify:
    * Previous bill(s) paid within due date?
    * Bill not received before due date (proven delivery issues)?
3.  If valid reason for potential waiver (or policy allows):
    * Raise Reverse Late Payment Charges ticket.
    * Status: BO Pending (Verify Late Payment Charges).
    * Inform TAT (6 DAYS).

**CRM Tagging/ Ticket Creation**

**Note:**
2% LPC (or applicable rate) if paid after due date. LPC appears in next bill. For waiver, ticket raised once LPC posted by Finance.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation
* **Marketing & Finance:** Verification, approval for reversal (if applicable), Ticket closure

## Refund
<!-- synonyms: Refund | रिफंड | सुरक्षा जमा वापसी | refund | security refund | deposit return | जमा वापसी -->
This section explains the 'Refund' process for security deposits or excess payments.

| **Category** | **Dom Service Requests** |
| ------------------ | --------------------------------------------------------------- |
| **Ticket Type** | **Refund** |
| **When** | **Customer wants Refund of security deposit or excess payment** |
| **TAT** | **12 DAYS** (after all documents received and final bill generated) |
| **Status Reasons** | 1. **BO Pending (Refund Requested by Customer - Security Deposit)** <br> 2. **BO Pending (Excess Payment Refund)** |

**Procedure:**
1.  Customer asks for Refund.
2.  **Security Deposit Refund (post Permanent Disconnection):**
    * Check if connection Permanently Disconnected in CRM.
        * **No:** Guide for PD first. If PD in process, tag Query Service.
        * **Yes:** Check if Final Bill generated.
            * **No:** Ask to wait for final bill. Update Query Service.
            * **Yes:** Guide customer to email to [customercare.png@igl.co.in](mailto:customercare.png@igl.co.in): PD job sheet, Refund form, Cancelled cheque/passbook copy.
            * Email Team verifies docs, raises Refund ticket. Status: BO Pending (Refund Requested by Customer). TAT (12 DAYS).
3.  **Excess Payment Refund:**
    * Verify excess payment in CRM.
    * Guide customer to email necessary documents (payment proof, cancelled cheque) to [customercare.png@igl.co.in](mailto:customercare.png@igl.co.in).
    * Email Team verifies, raises Refund ticket. Status: BO Pending (Excess Payment Refund). TAT (12 DAYS).

**CRM Tagging/ Ticket Creation (Primarily by Email Team)**

**Notes:**
1.  For security deposit refund, if Final Bill not generated, update customer to wait.
2.  If cancelled cheque has full name details and refund form issue, ticket might be raised without form (exception, subject to approval).
3.  If final bill unpaid, outstanding adjusted against security deposit; balance refunded.
4.  Refund of security amount (SD), ACSD. Installation charges (pre-2009) generally not refundable.

**Responsible Department:**
* **Call Center Operations (Email Team):** document verification, Ticket creation
* **Marketing:** Processing refund, coordination with Finance, Ticket Closure
* **Finance:** Fund transfer

## Retail Invoice Generation (RIG)
<!-- synonyms: Retail Invoice Generation (RIG) | खुदरा बिल जनरेशन | retail invoice generation | rig | retail bill | रिटेल बिल | रिटेल इनवॉइस -->
This section details 'Retail Invoice Generation' (RIG) to replace estimated bills with actual reading bills.

| **Category** | **Dom Service Requests** |
| ------------------ | ------------------------------------------------------------------- |
| **Ticket Type** | **Retail Invoice Generation** |
| **When** | **Customer wants to generate bill or replace Estimated Invoice with retail one based on actual reading** |
| **TAT** | **10 DAYS** |
| **Status Reasons** | 1. **On call meter reading submitted** <br> 2. **On WhatsApp meter reading submitted** <br> 3. **On Email meter reading submitted** <br> 4. **Meter reader visit requested** |

**Procedure:**
1.  Customer received Estimated Bill, wants Retail Invoice.
2.  Check last invoice date/due date.
3.  Ask for current meter reading. Check against last Retail Invoice reading; confirm meter no.
4.  **Customer provides reading (Call, WhatsApp, Email):**
    * Collect reading (must be > last retail invoice reading).
    * Confirm Meter no. (must match system). Note date of Reading.
    * Detail in Problem description. Status: (select appropriate).
    * Raise RIG ticket. TAT (10 DAYS).
5.  **Customer no share reading / requests meter reader visit:**
    * Status: Meter reader visit requested.
    * Raise RIG ticket. TAT (10 DAYS).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Suggest Self-Billing for faster bill if available.
2.  If reading not shared on call, request WhatsApp/email before Meter Reader Visit.
3.  Check payment status; guide to pay estimated bill (if reading cannot be provided, e.g. house locked), adjusts in next retail bill.
4.  WhatsApp/Email agent verify details before ticket. For reading variance, WMR may be needed.
5.  If previous invoice retail & within due date, ask to wait for portion billing.
6.  If PD/TD/ED lock active & customer using gas wants bill, lock removal needed before RIG.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation
* **Marketing:** Meter reading updation/verification
* **Finance:** Invoice generation
* **Ticket closure:** Marketing

## Rubber Tube Replacement
<!-- synonyms: Rubber Tube Replacement | रबर ट्यूब बदलना | rubber tube replacement | rubber pipe | रबर पाइप | pipe change | पाइप बदलना -->
This section covers 'Rubber Tube Replacement' requests.

| **Category** | **Dom Service Requests** |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| **Ticket Type** | **Rubber Tube Replacement** |
| **When** | **Customer wants Rubber tube replacement, Or wants to connect/remove rubber tube from stove.** |
| **TAT** | **2 DAYS** |
| **Status Reasons** | 1. **BO Pending (Pending Rubber Tube Replacement)** |

**Procedure:**
1.  Customer asks to replace/connect/remove Rubber Tube.
2.  Raise Rubber Tube Replacement ticket.
3.  Inform Charges: **1m tube:** Rs. 126.90; **1.5m tube:** Rs. 139.00; **Installation:** Rs. 82.31.
4.  Status: BO Pending (Pending Rubber Tube Replacement).
5.  Inform TAT (within 2 Days).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  IGL no provide tube > 1.5m. Customer can buy; IGL charges installation (Rs. 82.31 or prevailing).
2.  Review lead status for new connections. Probe if new setup or replacement. Not an NG case.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation
* **O&M:** Site visit and replacement/installation
* **Marketing:** Inducing charges and Ticket closure

## Defective Meter
<!-- synonyms: Defective Meter | खराब मीटर | defective meter | faulty meter | meter faulty -->
This section describes handling of 'Defective Meter' complaints.

| **Category** | **Dom Complaints** |
| ------------------ | ------------------------------------------------------------------------------------------------ |
| **Ticket Type** | **Defective Meter** |
| **When** | **Customer complains Meter running fast or Meter not working, foggy display** |
| **TAT** | **36 DAYS** (includes potential testing/replacement)                      |
| **Status Reasons** | 1. **BO Pending (Meter Not Working)** <br> 2. **BO Pending (Meter Running Fast)** |

**Procedure:**
1.  Customer concern about Meter. Clarify: **Meter not working** OR **Meter running fast**.
2.  Raise Defective Meter ticket.
    * **Meter not working (Smoky, display problem, readings not moving):**
        * Status: BO Pending (Meter not working).
        * Service Charge: Free (for replacement if found defective by IGL).
    * **Meter allegedly running fast:**
        * Suggest self-testing (capture readings over few days).
        * If customer insists faulty: Status: BO Pending (Meter running fast). Inform potential charges: Rs. 950/- Penalty + Rs. 343/- Testing charge (IF meter NOT found faulty by IGL).
3.  Inform TAT (36 DAYS).

**CRM Tagging/ Ticket Creation**

**Note:**
Meter may be inspected/changed. Post inspection/lab testing, billing analysis and adjustment if meter confirmed defective by IGL.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation
* **O&M:** Site work (inspection, replacement)
* **Marketing Team:** Billing analysis (if adjustment needed) & Ticket closure

## Incorrect Meter Number
<!-- synonyms: Incorrect Meter Number | गलत मीटर नंबर | incorrect meter number | meter no wrong | meter number error -->
This section covers complaints about an 'Incorrect Meter Number' in IGL records or bills.

| **Category** | **Dom Complaints** |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Ticket Type** | **Incorrect Meter Number** |
| **When** | **Meter number in IGL system/bill and at customer’s premise does not match** |
| **TAT** | **10 DAYS** |
| **Status Reasons** | 1. **BO Pending (Pending Meter Number Verification)** |

**Procedure:**
1.  Meter no. incorrect in Invoice/Lead Status or customer complains.
2.  Verify customer's reported meter no. against CRM. Validate address, esp. floor/apt no.
3.  Raise Incorrect Meter Number ticket.
4.  Status: BO Pending (Pending Meter Number Verification).
5.  Inform TAT (10 DAYS).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Issue common in multi-floor/apartments. Validate floor with customer.
2.  Once meter validated at site by Projects/O&M, details updated in CRM, bill revised if needed.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation
* **O&M (or Projects if initial error):** Site verification
* **Marketing Team:** CRM Correction, bill revision coordination, Ticket closure.

## Billed Without Gas Supply
<!-- synonyms: Billed Without Gas Supply | गैस आपूर्ति बिना बिल | billed without gas supply | no gas billed | गैस बिना बिल | supply off billing -->
This section details how to handle cases where a customer is 'Billed Without Gas Supply'.

| **Category** | **Dom Complaints** |
| ------------------ | ----------------------------------------------------------------------- |
| **Ticket Type** | **Billed Without Gas Supply** |
| **When** | **Customer complains for Bill generation but gas supply is not active** |
| **TAT** | **10 DAYS** |
| **Status Reasons** | 1. **BO Pending (Permanent Disconnection Check Pending)** <br> 2. **BO Pending (Billing Lock Pending)** <br> 3. **BO Pending (Installation Verification Pending)** |

**Procedure:**
1.  Customer billed despite no active gas supply.
2.  Analyze bill: consumption post TD/PD? Or NG never completed?
3.  **Bill post PD:** Check PD ticket status. Verify billing lock. Status: BO Pending (Permanent Disconnection Check Pending) or BO Pending (Billing Lock Pending).
4.  **Bill post TD:** Check TD ticket status. Verify billing lock from TD date. Status: BO Pending (Billing Lock Pending).
5.  **Bill generated, NG not done:** Check lead status. Status: BO Pending (Installation Verification Pending).
6.  Raise "Billed Without Gas Supply" ticket. Detail concern in Problem description.
7.  Inform TAT (10 DAYS).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Check PD/TD ticket. If lock missing, escalate for lock & bill revision.
2.  Verify meter number to rule out crossed connections.
3.  For TD, one last bill generated up to TD date. Check if disputed bill is this or subsequent.

**Responsible Department:**
* **Call Center Operations:** Ticket creation
* **Projects:** Installation verification (if NG not done)
* **Marketing Team:** Verification, correction (billing lock, bill revision), Ticket closure
* **Finance Team:** Bill reversal/adjustment processing.

## Arrears in Billing
<!-- synonyms: Arrears in Billing | बकाया बिल | arrears in billing | बकाया | due amount | outstanding bill | arrear charges -->
This section describes how to handle 'Arrears in Billing' issues, including unupdated payments or payments to wrong accounts.

| **Category** | **Dom Complaints** |
| ------------------ | ------------------------------------------------------------------------------------- |
| **Ticket Type** | **Arrears in Billing** |
| **When** | **Payment done but not updated in system or paid on wrong BP** |
| **TAT** | **8 DAYS** |
| **Status Reasons** | 1. **BO Pending (Payment Not Found)** |

**Procedure:**
1.  Check CRM if customer-claimed payment reflects.
    * **Payment in CRM, made after due date:** Inform payment received late, LPC might apply.
    * **Payment claimed, not in CRM:**
        * Inform customer to email Payment Proof to [customercare.png@igl.co.in](mailto:customercare.png@igl.co.in) (Mode, Date, Amount, Bank, Transaction ID/Cheque no./Receipt).
        * Email Team verifies proof. If valid & payment not found, raises "Arrears in Billing" ticket. Status: BO Pending (Payment Not Found). TAT (8 DAYS post ticket).
    * **Paid on wrong BP:** Request details of wrong/correct BP & proof. Email team raises ticket on *correct* BP. Status: BO Pending (Payment Not Found - to be transferred).

**CRM Tagging/ Ticket Creation (Primarily by Email Team)**

**Notes:**
1.  Transaction proof mandatory (ID, BBPS ID for online; debit details/cheque no for cheque; bank receipt for cash).
2.  For payment on wrong BP, customer shares reason, all transaction details. Ticket on correct B.P.

**Responsible Department:**
* **Call Center Operations (Email Team):** proof verification, Ticket creation
* **Finance Team & Marketing Team:** Payment updation, transfer, reconciliation & Ticket closure

## Name and Address Correction
<!-- synonyms: Name and Address Correction | नाम और पता संशोधन | name address correction | नाम पता सुधार | address change | name change | पता परिवर्तन -->
This section outlines the process for 'Name and Address Correction' in IGL records.

| **Category** | **Dom Service Requests** |
| ------------------ | ---------------------------------------------------------------------------- |
| **Ticket Type** | **Name and Address Correction** |
| **When** | **Customer wants to correct error in Name/ Address in system** |
| **TAT** | **5 DAYS** (after valid documents receipt)                            |
| **Status Reasons** | 1. **BO Pending (Pending Name/ Address Correction)** |

**Procedure:**
1.  Customer wants Name/Address correction (typographical, minor change).
2.  Advise customer to email documents to [customercare.png@igl.co.in](mailto:customercare.png@igl.co.in) or [updatekyc@igl.co.in](mailto:updatekyc@igl.co.in):
    * **Name Correction:** ID proof (correct Name), Ownership Proof, BP no.
    * **Address Correction (minor):** Ownership proof (correct address), BP no.
3.  Email Team verifies docs. If valid, raises "Name and Address Correction" ticket.
4.  Status: BO Pending (Pending Name/Address Correction). TAT (5 DAYS post ticket).

**CRM Tagging/ Ticket Creation (Primarily by Email Team)**

**Notes:**
1.  Minor spelling/landmark errors: email [updatekyc@igl.co.in](mailto:updatekyc@igl.co.in) from registered email. TAT 5 days.
2.  Significant changes (tower/block): proper address/ownership proof. If implies ownership change, guide for that.

**Responsible Department:**
* **Call Center Operations (Email Team):** document verification, Ticket creation
* **Marketing Team:** Verification, updating CRM, Ticket closure

## Modification- Geyser/ Extra Point
<!-- synonyms: Modification- Geyser/ Extra Point | गीजर / अतिरिक्त पाइंट संशोधन | modification geyser extra point | geyser point | extra point | गीजर पाइपिंग | अतिरिक्त पाइंट -->
This section details requests for 'Modification- Geyser/ Extra Point'.

| **Category** | **Dom Service Request** |
| ------------------ | ---------------------------------------------------------------------------------- |
| **Ticket Type** | **Modification- Geyser/ Extra Point** |
| **When** | **Customer wants an Extra point/ Geyser connection on same floor where using PNG** |
| **TAT** | **8 DAYS** |
| **Status Reasons** | 1. **BO Pending (Customer Req. Modification)** |

**Procedure:**
1.  Customer asks for extra PNG point/Geyser connection on same floor.
2.  **Do not commit** for extra point; feasibility checked by technicians at site.
3.  Raise Modification – Geyser / Extra point ticket.
4.  Status: BO Pending (Customer Req. Modification).
5.  Inform charges confirmed by technician after site survey.
6.  Inform TAT (8 DAYS for site visit/quotation).

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Additional point in same kitchen: raise Mod/Geyser Extra Point.
2.  Max 2 points per connection on same floor (subject to policy/feasibility).
3.  Point in different kitchen (same floor, structurally separate) or other floor: new connection needed.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation
* **O&M:** site survey, feasibility, execution
* **Marketing Team:** Inducing charges, Ticket closure

## Restoration with Device
<!-- synonyms: Restoration with Device | मीटर के साथ पुनःस्थापन | restoration with device | meter reinstall | उपकरण सहित पुनः स्थापना -->
This section covers 'Restoration with Device' after a temporary disconnection for renovation where the device was removed by IGL.

| **Category** | **Dom Service Request** |
| ------------------ | --------------------------------------------------------------- |
| **Ticket Type** | **Restoration with Device** |
| **When** | **Customer wants Restoration post TD Renovation (with device removed by IGL)** |
| **TAT** | **6 DAYS** |
| **Status Reasons** | 1. **BO Pending (Request Restoration by Customer)** |

**Procedure:**
1.  Customer asks for meter restoration.
2.  Check if **TD- Renovation (with device removal)** ticket previously raised & completed.
    * If yes: Raise Restoration with Device ticket. Status: BO Pending (Requested Restoration by Customer). Inform charges confirmed by Technician. TAT (6 DAYS).
    * **Defaulter Disconnected:** Follow Defaulter Restoration process.
    * **No relevant TD Renovation (with device) ticket:** Probe. May need Mod-GI.

**CRM Tagging/ Ticket Creation**

**Note:**
If TD request (device taken by IGL) exists and customer requests restoration, use this ticket. If pipes need re-routing, may be Mod-GI.

**Responsible Department:**
* **Call Center Operations:** for Ticket creation
* **O&M:** execution (re-installing meter/GI pipe)
* **Marketing Team:** Inducing charges, Ticket closure

## Restoration without Device Installed
<!-- synonyms: Restoration without Device Installed | मीटर बिना पुनःस्थापन | restoration without device | no device restoration | बिना उपकरण पुनः स्थापना -->
This section details 'Restoration without Device Installed', typically after a TDPR or TD Renovation where the meter wasn't removed.

| **Category** | **Dom Service Request** |
| ------------------ | ------------------------------------------------------------------------- |
| **Ticket Type** | **Restoration without Device Installed** (Meter not removed by IGL, supply stopped at valve) |
| **When** | **Customer wants Restoration post TD Renovation (without device removal by IGL) / TDPR** |
| **TAT** | **6 DAYS** |
| **Status Reasons** | 1. **BO Pending (Requested Restoration by Customer)** |

**Procedure:**
1.  Customer asks to restore connection/pipelines.
2.  Check if **TD-Personal Reason** OR **TD Renovation-without device removal** ticket previously raised & completed.
3.  If yes (and billing lock active):
    * Raise Restoration Without Device Installed ticket.
    * Status: BO Pending (Requested Restoration by Customer).
    * Inform applicable charges (visit charge, pending monthly TD charges).
    * TAT (6 DAYS).
4.  If no such TD ticket, probe reason for no supply.

**CRM Tagging/ Ticket Creation**

**Responsible Department:**
* **Call Center Operations:** for Ticket creation
* **O&M:** execution (opening valve, safety check)
* **Marketing Team:** Removing billing lock, inducing charges, Ticket closure

## Ownership Transfer
<!-- synonyms: Ownership Transfer | स्वामित्व हस्तांतरण | ownership transfer | नामांतरण | transfer of ownership | transfer connection | कनेक्शन हस्तांतरण -->
This section outlines the comprehensive 'Ownership Transfer' process for IGL connections.

| **Category** | **Dom Service Request** |
| ------------------ | ---------------------------------------------------- |
| **Ticket Type** | **Ownership Transfer** |
| **When** | **Customer wants Ownership Transfer** |
| **TAT** | **14 DAYS** (Individual Name, post-docs); **5 DAYS** (Builder KYC, post-docs to email) |
| **Status Reasons** | **BO Pending (Information Provided to Customer)**; **BO Pending (Documents under Verification)** |

**Procedure:**
1.  Customer calls for Ownership Transfer. Confirm Reason (Sale/Purchase, Death, Name Add/Reduction) & Connection Name type.
2.  **Builder Name (Builder KYC):**
    * Guide Customer to email scanned: IGL Form, ID Proof, Ownership Proof, Meter Photo, Co-owner consent (if joint property) to [pngbuilders@igl.co.in](mailto:pngbuilders@igl.co.in).
    * TAT: Approx. 5 days post email.
3.  **Individual Name:**
    * Guide on docs (see table below): IGL Form, New owner ID & Ownership Proof, NOC (Type A/B/C), Meter Photo. Death Cases: Death cert, Regd. Will/Relinquishment Deed.
    * Docs: Soft copy to [customercare.png@igl.co.in](mailto:customercare.png@igl.co.in); Hard copy to IGL Marketing, Noida.
    * TAT: 14 Days (post correct hardcopy docs).
4.  Check outstanding dues; inform customer to clear.
5.  Log initial query. Update status once docs received.

This table summarizes key documents required for individual name transfers based on reason.
| **OWNERSHIP TRANSFER REASON** | **KEY DOCUMENTS REQUIRED (Individual Name Transfers)** |
| :-------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purchase of Property (Previous Owner Available)** | 1. IGL [PNG Ownership Transfer Form](https://www.iglonline.net/5000_media/PNG%20Ownership%20Transfer%20Form.pdf). <br> 2. **ID proof** new owner. <br> 3. **NOC (TYPE-A)** from prev. owner (Rs. 100/- Stamp, Notarized). <br> 4. **Ownership Proof** new owner (Regd. Sale deed/Conveyance Deed OR Latest Electricity Bill). <br> 5. Meter Photo. |
| **Absence of NOC from previous owner** | 1. IGL Form. <br> 2. **ID proof** new owner. <br> 3. **NOC (TYPE-B)** (Rs. 100/- Stamp, Notarized, self-declaration/indemnity). <br> 4. **Ownership Proof:** Court order (clear title) or Auction letter. <br> 5. Meter Photo. |
| **Death of existing holder / Inheritance / Succession** | 1. IGL Form. <br> 2. **ID proof** new owner/heir. <br> 3. **NOC (Type-C)** (Rs. 100 Stamp, Notarized, from other heirs/self-declaration). <br> 4. **Death certificate**. <br> 5. Copy **Regd. Will** OR **Regd. Relinquishment Deed**. <br> 6. Meter Photo. <br> \*\* Multiple heirs in regd. will: NOC from others (Rs. 100 stamp, notarized). |

**Link:** [Indraprastha Gas Limited - Ownership Transfer](https://www.iglonline.net/english/Default.aspx?option=article&type=single&id=200&mnuid=380&prvtyp=site)

**Note:**
Outstanding dues should be cleared.

**Responsible Department:**
* **Call Center Ops:** Initial guidance, logging query.
* **Marketing Team:** Doc verification, processing, CRM update, Ticket closure.
* **Finance Team:** Dues & security deposit management.

## Improper Installation
<!-- synonyms: Improper Installation | गलत इंस्टॉलेशन | improper installation | installation issue | installation faulty -->
This section covers complaints related to 'Improper Installation' of IGL equipment or pipelines.

| **Category** | **Dom Complaints** |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| **Ticket Type** | **Improper Installation** |
| **When** | **Customer wants proper Installation or complains about dissatisfaction with recent installation.** |
| **TAT** | **3 DAYS** (initial response/visit scheduling)                                                           |
| **Status Reasons** | 1. **BO Pending (Installation Check Pending - O&M)** <br> 2. **BO Pending (Installation Check Pending - Projects)** |

**Procedure:**
1.  Customer complains of dissatisfaction with IGL installation service (pipelines/meter improperly installed, against consent, unsafe).
2.  Probe reason for dissatisfaction. Check last service (New Connection, Mod, Reconnection).
3.  Bifurcate: **Project team** (new connections, major mods pre-NG) or **O&M team** (post-connection mods, repairs).
4.  Raise Improper Installation ticket.
    * O&M work: Status: BO Pending (Installation Check Pending - O&M).
    * Projects work: Status: BO Pending (Installation Check Pending - Projects).
5.  Inform TAT (3 Days for investigation).

**CRM Tagging/ Ticket Creation**

**Note:**
Customer should report promptly post-installation.

**Responsible Department:**
* **Call Center Operations:** Ticket creation.
* **Projects & O&M:** Site visit, investigation, corrective work, Ticket closure feedback.
* **Marketing/Coordination:** May facilitate closure.

## No Gas Supply
<!-- synonyms: No Gas Supply | गैस आपूर्ति बंद | no gas supply | गैस नहीं | gas supply off | supply closed | कोई गैस आपूर्ति -->
This section details the emergency procedure for 'No Gas Supply'.

| **Category** | **Dom Emergency** |
| ------------------ | ------------------------------------------ |
| **Ticket Type** | **No Gas Supply** |
| **When** | **Customer complains for No Gas Supply** |
| **TAT** | **30 min. – 3 Hours** (visit/restoration) |
| **Status Reasons** | 1. **BO Pending (Pending Supply Restore)** |

**Procedure:**
1.  Customer complains No Gas Supply.
2.  Probe: New stove changed/connected? Valves closed?
3.  If no stove change, valves open (or unsure/unable to check), unexpected stoppage:
    * Raise No Gas Supply ticket. Status: BO Pending (Pending Supply Restore). TAT (30 min - 3 hours).
    * After raising ticket, CSR calls Customer’s allocated Control Room.

**CRM Tagging/ Ticket Creation**

**Note:**
Known line damage/planned maintenance: update affected callers on tentative restoration time. No individual tickets unless instructed.

**Responsible Department:**
* **Call Center Operations:** Ticket creation and immediate Control Room intimation.
* **O&M / Control Room:** Dispatch, site work, Ticket closure.

## Leakage
<!-- synonyms: Leakage | गैस लीकेज | leakage | gas leak | gas leakage | गैस रिसाव -->
This section outlines the critical emergency procedure for reporting 'Leakage'.

| **Category** | **Dom Emergency** |
| ------------------ | --------------------------------------------------------- |
| **Ticket Type** | **Leakage** |
| **When** | **Customer complains for smell, Leakage, fire, etc.** |
| **TAT** | **30 min. – 3 Hours** (visit/arresting leakage)       |
| **Status Reasons** | 1. **BO Pending (Pending Leakage Arrest)- GI** <br> 2. **BO Pending (Pending Leakage Arrest)- MDPE** |

**Procedure:**
1.  Customer complains Gas Leakage.
2.  **Show Empathy. Immediately share safety parameters:** Close Isolation/Appliance Valve IF SAFE. Do NOT operate Electric Switches. Open doors/windows for Ventilation. Evacuate if strong smell.
3.  Try to confirm Leakage point (GI/MDPE pipe? Downstream/Upstream? Meter-Appliance Valve? After Appliance Valve?).
4.  Raise Leakage ticket. Status: BO Pending (Pending Leakage Arrest)- GI or MDPE. TAT (30 min - 3 hours).
5.  After raising ticket, CSR calls Customer’s allocated Control Room.

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Agent MUST empathize and state safety guidelines first.
2.  Agent to immediately call Control Room.

**Responsible Department:**
* **Call Center Operations:** Ticket creation and immediate Control Room intimation.
* **O&M / Control Room:** Dispatch, site work (arresting leakage, repairs).
* **Marketing Team:** Billing analysis (if excess consumption due to leak).
* **Finance Team:** Adjustments (if any).
* **Ticket closure:** O&M (technical); Marketing (billing-related).

## Site Related (Malba / Debris Removal)
<!-- synonyms: Site Related (Malba / Debris Removal) | मलबा हटाना | debris removal | site debris | malba issue -->
This section covers complaints regarding 'Site Related (Malba / Debris Removal)' after IGL work.

| **Category** | **Dom Complaint** |
| ------------------ | ----------------------------------------------------------------- |
| **Ticket Type** | **Site Related (Malba)** |
| **When** | **Customer complaints remaining malba/debris at site after IGL work** |
| **TAT** | **3 DAYS** |
| **Status Reasons** | 1. **BO Pending (Malba Removal Pending)** |

**Procedure:**
1.  Customer wants malba removal post IGL work (usually Projects Dept).
2.  User or Non-User?
    * **User:** Raise Site Related (Malba) ticket. Status: BO Pending (Malba Removal Pending). Charges: N/A. TAT (3 Days).
    * **Non-User:** Confirm Name, Address, Mobile. Escalate to supervisor for Projects team.

**CRM Tagging/ Ticket Creation**

**Notes:**
1.  Non-user concerns: Supervisor sends to Internal Team (Projects).

**Responsible Department:**
* **Call Center Operations:** Ticket creation.
* **Projects:** Debris removal & Ticket closure.

## NOC (No Objection Certificate)
<!-- synonyms: NOC (No Objection Certificate) | एनओसी | noc | noc letter | अनापत्ति प्रमाणपत्र | noc certificate -->
This section explains requests for a 'No Objection Certificate' (NOC) from IGL.

| **Category** | **Dom Request/Information** |
| ------------------ | -------------------------------------------------------------- |
| **Ticket Type** | **NOC Request** |
| **When** | **Customer requested for NOC.** |
| **TAT** | **Varies.** |

**Handling NOC Requests:**

1.  Probe reason and connection type.
2.  **Private Connection:** Generally, IGL **denies/does not provide** NOC for private connections (ownership transfer process followed instead).
3.  **Government Connection:**
    * **Active Customer (NGC done):**
        1.  Permanent Disconnection process.
        2.  Final Bill generation.
        3.  Payment of Final Bill (if dues after SD adjustment).
        4.  Post payment, NOC issued (Govt. dept liaises with IGL).
    * **Non-Active Customer (Never applied/NGC never done/NOC for other purposes):**
        * Ask to visit Control Room/designated office with: Allotment Letter, Self-ID Proof, Meter Photo (if exists), Formal request letter.
        * Process depends on specific NOC type.

**CRM Tagging / Ticket creation:**
* Log as "Query Service" or "NOC Request". Capture details.
* Complex Govt. NOCs may be forwarded internally.

**Responsible Department:**
* **Call Center Operations:** Initial guidance, ticket creation.
* **Marketing / Commercial Dept:** Processing and generating NOC (mostly Govt.).
* **Finance Dept:** No dues confirmation.
* **Ticket closure:** Marketing/Commercial Dept.

## Role of Internal Note & Quick follow up
<!-- synonyms: Role of Internal Note & Quick follow up | आंतरिक नोट | quick follow up | internal note | क्विक फ़ॉलोअप -->
This section explains the procedure for using internal notes and quick follow-ups for existing tickets or leads.

**Handling follow-up calls on existing tickets:**

1.  Customer follows up. Check CRM for ticket using BP no./ticket no.
2.  Review status/remarks.
    * **Closed Ticket:** Update customer with resolution. Do **not** update note. If issue persists, new ticket or reopen (if policy allows short timeframe).
    * **Open Ticket:** Inform current status. If new info/pressing concern: Edit ticket, Update **Internal Note** (calling no., date, concern), Save. Mark **Quick Follow Up**. Request to wait if within TAT, unless critical update.
3.  **New Connection Lead Follow-up:** Capture info in **Lead Internal Note**. Mark Quick Follow Up on Lead if action needed.

## Lead Creation
<!-- synonyms: Lead Creation | लीड क्रिएशन | lead creation | lead gen | लीड बनाना | lead generation -->
This section outlines the steps for 'Lead Creation' in CRM after a BP number is generated for a new connection.

After creating BP number in CRM, to create a lead:

1.  Navigate to Lead creation in CRM. Associate with BP number.
2.  Fill Lead Details (customer info, address, contact, connection type). Capture notes.
3.  Save Lead. Initial status e.g. – **Document submission pending**.
4.  Inform customer of required documents and submission process.

## DOMESTIC QUERY (General Query Handling)
<!-- synonyms: DOMESTIC QUERY (General Query Handling) | घरेलू क्वेरी | domestic query | query handling | dom query | घरेलू प्रश्न | सामान्य पूछताछ -->
This section describes how 'DOMESTIC QUERY' tickets are used for various general customer inquiries.

| **Category** | **Dom Service Request / Information** |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Ticket Type** | **Query** (with sub-types)                                                                                                           |
| **When** | **Customers seek information on connection, IGL products/services, procedures, bills, payments etc.** |
| **TAT** | **24 hrs / 1 Day** (query resolution/first response)                                                           |
| **Status Reasons** | Choose as per concern (e.g., Information Provided). Capture details in internal note. Share info. |

**Based on Query Type:**

1.  **General info on existing connection/status or general IGL info:** Raise “**Dom Query Service**”.
2.  **Info on IGL products/services (stove compatibility, geyser info):** Raise “**Dom Query Product**”.
3.  **Info on service request procedure/charges/documentation:** Raise “**Dom Query Service Request Procedure**”.
4.  **Info on new connection process/documentation:** Raise “**Dom Query New Connection Procedure**”.
5.  **Info on o/s, consumption, bill components/EMI/charges:** Raise “**Dom Query Understand Bill**”.
6.  **Info on Final Bill (post disconnection):** Raise “**Dom Query Final Bill**”.
7.  **Info on payments status/payment modes:** Raise “**Dom Query Payment Options**”.

**Responsible Department:**
* **Call Center Operations:** Ticket creation and resolution.
* **Call Center Operations:** Ticket closure.