import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Email you want to send the update from (only works with gmail)
fromEmail = '******@gmail.com'
# You can generate an app password here to avoid storing your password in plain text
# https://support.google.com/accounts/answer/185833?hl=en
fromEmailPassword = '*****'

# Email you want to send the update to
toEmail = '*******@gmail.com'


def sendEmail(unknown):
    img_data = open(unknown, 'rb').read()
    # msg = MIMEMultipart()
    # msg['Subject'] = 'subject'
    # msg['From'] = 'e@mail.cc'
    # msg['To'] = 'e@mail.cc'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Security Update'
    msgRoot['From'] = fromEmail
    msgRoot['To'] = toEmail
    msgRoot.preamble = 'Raspberry pi security camera update'

    text = MIMEText("test")
    msgRoot.attach(text)
    image = MIMEImage(img_data, name=os.path.basename("unknown/Unknown." + str() + ".jpg"))
    msgRoot.attach(image)

    # s = smtplib.SMTP(Server, Port)
    # s.ehlo()
    # s.starttls()
    # s.ehlo()
    # s.login(UserName, UserPassword)
    # s.sendmail(From, To, msg.as_string())
    # s.quit()

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(fromEmail, fromEmailPassword)
    smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
    # smtp.quit()
