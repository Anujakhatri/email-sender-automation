import argparse
import os
import csv
from email_sender.sender import send_email, run_bulk_send
from email_sender.config import EMAIL_USER

def retry_failed(template_name="template.html", subject="Retry Failed Message"):
    failed_csv = "output/failed_recipients.csv"
    if not os.path.exists(failed_csv):
        print("No failed recipients found.")
        return

    to_retry = []
    with open(failed_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('email'):
                to_retry.append(row['email'])
                
    if not to_retry:
        print("No emails to retry.")
        return
        
    # Remove duplicates
    to_retry = list(set(to_retry))
    
    # Back up the old failed log and create a new one
    os.rename(failed_csv, f"output/failed_recipients_backup_{int(os.path.getmtime(failed_csv))}.csv")
    
    print(f"Retrying {len(to_retry)} failed emails...")
    for email in to_retry:
        send_email(recipients=[email], subject=subject, template_name=template_name)

def main():
    parser = argparse.ArgumentParser(description="Email Sender Automation")
    parser.add_argument("--bulk", action="store_true", help="Send emails to all contacts in data/contacts.csv")
    parser.add_argument("--retry-failed", action="store_true", help="Retry sending to failed recipients")
    args = parser.parse_args()

    if args.bulk:
        print("Starting bulk send...")
        run_bulk_send()
        print("Bulk send completed.")
    elif args.retry_failed:
        print("Retrying failed sends...")
        retry_failed()
        print("Retry completed.")
    else:
        print(f"Sending default test email to {EMAIL_USER}...")
        send_email()
        print("Test email completed.")

if __name__ == "__main__":
    main()
