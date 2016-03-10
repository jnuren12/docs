import smtplib
message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
smtp = smtplib.SMTP('localhost')
smtp.sendmail('from@fromdomain.com', ['to@todomain.com'], message)
