import csv
import os
from datetime import datetime

OUTPUT_DIR = "output"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def log_sent(email, subject):
    ensure_output_dir()
    filepath = os.path.join(OUTPUT_DIR, "sent_log.csv")
    file_exists = os.path.exists(filepath)
    with open(filepath, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "email", "subject"])
        writer.writerow([datetime.now().isoformat(), email, subject])

def log_failed(email, error_message):
    ensure_output_dir()
    filepath = os.path.join(OUTPUT_DIR, "failed_recipients.csv")
    file_exists = os.path.exists(filepath)
    with open(filepath, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "email", "error"])
        writer.writerow([datetime.now().isoformat(), email, error_message])
