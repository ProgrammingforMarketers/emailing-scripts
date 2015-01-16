import gspread

GMAIL_USERNAME = "YOUR USERNAME"
GMAIL_PASSWORD = "YOUR PASSWORD"
recipients = ["recipient1@example.com", "recipient2@example.com"]

'''
Uncomment this to send emails from a Google spreadsheet
gc = gspread.login(GMAIL_USERNAME, GMAIL_PASSWORD)
wks = gc.open("SPREADSHEET WITH EMAIL ADDRESSES NAME").sheet1

recipients = wks.col_values(COLUMN WITH EMAIL ADDRESSES NUMBER (Column A = 1, for example))
'''