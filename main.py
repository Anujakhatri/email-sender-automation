from email_sender.sender import send_email

def main():
    """CLI entry point for email sender automation"""
    print("Email Sender Automation")

    # Example usage
    subject = "Test Email"
    body = "This is a test project"

    # Send to yourself
    send_email(subject, body)

if __name__ == "__main__":
    main()