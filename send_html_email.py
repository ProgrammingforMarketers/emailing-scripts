import smtplib

# The below code never changes, though obviously those variables need values.
from gmail_variables import *


def sendEmail(recipient):
	email_subject = "ENTER AN EMAIL SUBJECT HERE"
	#recipient = "nat@programmingformarketers.com"

	body_of_email = "ENTER BODY OF EMAIL HERE, HTML OR TEXT"

	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.ehlo()
	session.starttls()
	session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

	headers = "\r\n".join(["from: " + GMAIL_USERNAME,
	                       "subject: " + email_subject,
	                       "to: " + recipient,
	                       "mime-version: 1.0",
	                       "content-type: text/html"])

	# body_of_email can be plaintext or html!                    
	content = headers + "\r\n\r\n" + body_of_email
	session.sendmail(GMAIL_USERNAME, recipient, content)

[sendEmail(i) for i in recipients]
