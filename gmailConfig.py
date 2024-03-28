import time
import smtplib, ssl
# Setting up the params for the E-mail server.
smtp_server = "smtp.gmail.com"
smtp_port = 465
senders_email = input("Please enter the senders e-mail address: ")
senders_password = input("Please input your Password: ")
receivers_email = input("Please input the recievers e-mail address: ")
message = """\

HEY TYRRICK IT'S CODING TIME!!

"""
# initializze the email sending.
def send_email(message):
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port, context) as server:
        server.ehlo()
        server.login(senders_email, senders_password)
        server.starttls()
        server.sendmail(senders_email, receivers_email, message)
        server.quit()