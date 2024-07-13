import smtplib,ssl #寄email的模組
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header 
sender="iversoner333@gmail.com"
receiver=["iversoner333@yahoo.com.tw","iversoner333@gmail.com"]
for i in receiver:

    msg = MIMEMultipart()
    msg["From"] =  sender #dictionary的概念,From大小寫有差
    msg["To"] = i
    header = Header("Test Send Email","utf-8")
    msg["Subject"] = header.encode()

    body = "This is email send from python"
    """msg.attach(MIMEText(body)) #和下面兩句同樣意思"""
    msg.attach(MIMEText(body)) #attach把前面設定的指派進去

    ssl_context= ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
        server.login (sender,"jazl eukr bxtm hiix")
        server.sendmail(sender,i,msg.as_string())
    print("success sent email")






