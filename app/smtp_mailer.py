import smtplib
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASS, REPLY_TO

def send_email(to_email, html_content, name):
    msg = MIMEText(html_content, "html")
    msg["Subject"] = f"Hi {name}, quick tips for your business"
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Reply-To"] = REPLY_TO

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
