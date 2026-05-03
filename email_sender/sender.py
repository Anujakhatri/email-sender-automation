import smtplib
import time
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email_sender.config import EMAIL_USER, EMAIL_PASS
from email_sender.logger import log_sent, log_failed
from email_sender.template_renderer import render_template

def _send_with_retry(msg, recipient, subject):
    attempts = 3
    for attempt in range(attempts):
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL_USER, EMAIL_PASS)
                server.send_message(msg)
            log_sent(recipient, subject)
            return True
        except Exception as e:
            if attempt < attempts - 1:
                time.sleep(2 ** attempt)  # Exponential backoff: 1s, 2s
            else:
                log_failed(recipient, str(e))
                return False

def send_email(recipients=None, subject="Automated Message", template_name="template.html", context=None, body_text=None):
    if recipients is None:
        recipients = [EMAIL_USER]
    elif isinstance(recipients, str):
        recipients = [recipients]
        
    for recipient in recipients:
        msg = MIMEMultipart('alternative')
        msg['From'] = EMAIL_USER
        msg['To'] = recipient
        msg['Subject'] = subject
        
        if body_text:
            msg.attach(MIMEText(body_text, 'plain'))
            
        if template_name:
            html_content = render_template(template_name, context)
            msg.attach(MIMEText(html_content, 'html'))
        
        _send_with_retry(msg, recipient, subject)

def run_bulk_send(csv_file="data/contacts.csv", template_name="template.html", subject="Bulk Automated Message", body_text=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, csv_file)
    
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row.get('email')
            if not email:
                continue
            
            msg = MIMEMultipart('alternative')
            msg['From'] = EMAIL_USER
            msg['To'] = email
            msg['Subject'] = subject
            
            if body_text:
                msg.attach(MIMEText(body_text, 'plain'))
                
            if template_name:
                # Use row data as context for personalization
                html_content = render_template(template_name, context=row)
                msg.attach(MIMEText(html_content, 'html'))
            
            _send_with_retry(msg, email, subject)
            time.sleep(1)  # Brief delay to prevent rate limiting
