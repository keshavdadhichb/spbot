from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pywhatkit as kit
import time

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)

sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1n-9Beu8EWjNcuwQLmxtugm8z6FNc-wjORElNyTdRFGc/edit#gid=0").sheet1

data = sheet.get_all_records()

message_template = ("Hey {name},\n"
                    "I'm Keshav from ACM-VIT, a leading technical chapter of VIT Vellore, India and we would like to partner with {company} "
                    "for Reverse Coding - our flagship competitive coding event scheduled on Feb 7, 2025 with an expected footfall of 600+ students, "
                    "most of them being from CSE branches.")

for row in data:
    name = row['Name']
    company = row['Company Name']
    phone = row['Phone Number']
    message = message_template.format(name=name, company=company)
    
    try:
        print(f"Sending message to {name} at {phone}...")
        kit.sendwhatmsg_instantly(f"+{phone}", message)
        print(f"Message sent to {name} successfully!")
    except Exception as e:
        print(f"Failed to send message to {name} ({phone}): {e}")
    
    time.sleep(10)
