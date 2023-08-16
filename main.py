# Import statments

import pandas as pd
from email.message import EmailMessage
import smtplib

# credentials of the sender email

email_sender = 'sumit.cerex@gmail.com'
email_password = 'yggvcdylkphlcmwr'

# opening the excel file to read the receivers email ids
df = pd.read_excel("E:\email_automation\mail [13001-end].xlsx")

email_receiver = df["Email"].values

subject = 'Approcach to design your logo' #subject of the email
# body of the email
body = """
hi
"""

zipped = zip(email_receiver)

# other way of diretly making a receivers list 
# ex = email_list = ["email_id_1", "email_id_2", "email_id_3", "email_id_4", "email_id_5"]

# now traversing through the list of email ids and sending the mails

for(a) in zipped:

    # setting the email contents
    msg = EmailMessage()
    msg[ 'From' ] = email_sender
    msg [ 'To' ] =a
    msg [ 'Subject' ] = subject
    msg.set_content(body)

    # getting logged in and sending the mail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp :
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)

# printing statement on successful execution
if __name__ == "__main__":
    print("Done")
