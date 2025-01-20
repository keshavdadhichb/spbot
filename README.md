# WhatsApp Automation for Sponsorships

This script automates the process of sending personalized WhatsApp messages to potential sponsors from a Google Sheet.

## Steps to Use

 **Prepare Your Google Sheet:**
   - Column A: Company Name
   - Column B: Name
   - Column C: Phone Number

 **Install PyWhatKit:**
   - Install the `pywhatkit` library:
     ```bash
     pip install pywhatkit
     ```
   - Customize the message template to suit your needs (e.g., sponsor details, event info).

   - The script reads data from your Google Sheet and sends WhatsApp messages to the phone numbers.

   - Test with a few rows first.
   - Ensure WhatsApp Web is open when using `pywhatkit`.
