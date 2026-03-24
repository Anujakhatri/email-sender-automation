import smtplib
from .config import EMAIL_USER, EMAIL_PASS

def send_email(subject: str, body: str, recipients: str = None):
    """
    Send an email via Gmail SMTP.

    Parameters:
        subject (str): Subject of the email
        body (str): Body of the email
        recipients (str or list, optional): Single email or list of emails.
    """

    if recipients is None:
        recipients = [EMAIL_USER]
    elif isinstance(recipients, str) :
        recipients = [recipients]
    message = f"Subject: {subject}\n\n{body}"

    print("Connecting to SMTP server...")
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        print("Starting TLS encryption...")
        server.starttls()
        print("Logging in...")
        server.login(EMAIL_USER, EMAIL_PASS)

        for recipient in recipients:
            print(f"Sending email to {recipient}...")
            server.sendmail(EMAIL_USER, recipient, message)

    print("Email sent successfully!")