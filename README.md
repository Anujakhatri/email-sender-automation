# 📧 Email Sender Automation

> Automated bulk email sender built with Python and SMTP. Features recipient management via CSV, dynamic HTML templates with personalisation, configurable send intervals, retry logic, and a full delivery report with success/failure tracking.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Output](#output)
- [Example CSV](#example-csv)
- [Example Email Template](#example-email-template)
- [Error Handling](#error-handling)
- [License](#license)

---

## 📖 About the Project

This is a Python automation project that sends **bulk marketing emails** using the SMTP protocol. Instead of manually sending emails one by one, this tool reads a list of recipients from a CSV file, personalizes each email using an HTML template, and delivers them automatically — while logging every result.

Built as part of a Python automation portfolio.

---

## ✨ Features

- ✅ Send bulk emails to hundreds or thousands of recipients
- ✅ Personalize each email using `{{name}}` placeholders
- ✅ Read recipients from a CSV file
- ✅ HTML email template support
- ✅ Configurable delay between sends (avoid spam filters)
- ✅ Retry logic for failed sends
- ✅ Delivery summary printed to console
- ✅ Full delivery log saved to `sent_log.csv`
- ✅ Failed recipients saved to `failed_recipients.csv`
- ✅ Credentials stored securely using `.env`

---

## 📁 Project Structure

```
email-sender-automation/
│
├── email_sender/                   # Core package
│   ├── __init__.py                 # Makes this a Python package
│   ├── sender.py                   # Core SMTP send logic
│   ├── template_renderer.py        # Renders HTML template per recipient
│   ├── logger.py                   # Logs sent/failed results to CSV
│   └── config.py                   # Loads .env settings
│
├── data/                           # Input files
│   ├── contacts.csv                # Your recipient list
│   └── template.html               # Your email body template
│
├── output/                         # Auto-generated on run (gitignored)
│   ├── sent_log.csv                # Full delivery log
│   └── failed_recipients.csv       # Failed sends for re-run
│
├── tests/                          # Unit tests
│   ├── test_sender.py
│   └── test_template_renderer.py
│
├── main.py                         # Entry point — runs the automation
├── .env                            # SMTP credentials (never commit this)
├── .env.example                    # Example env file (safe to commit)
├── .gitignore                      # Ignores .env, output/, __pycache__
├── LICENSE                         # MIT License
├── pyproject.toml                  # Build system config
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup for PyPI
└── README.md                       # Documention (This file)
```

---

## ⚙️ Requirements

- Python 3.8+
- A Gmail account (or any SMTP provider)
- Gmail App Password (if using Gmail with 2FA)

## 🔧 Installation

1. **Clone the repository**

```bash
git clone "URL"
cd email_sender-automation
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up your `.env` file**

```bash
cp .env.example .env
```

Then edit `.env` with your credentials:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=you@gmail.com
SENDER_PASSWORD=your_app_password_here
```

---

## 🔐 Configuration

| Variable | Description | Example |
|---|---|---|
| `SMTP_HOST` | Mail server address | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP port (TLS) | `587` |
| `SENDER_EMAIL` | Your sending email | `you@gmail.com` |
| `SENDER_PASSWORD` | App password or SMTP key | `xxxx xxxx xxxx xxxx` |

---

##  Usage

1. Add your recipients to `contacts.csv`
2. Edit your email body in `template.html`
3. Run the script:

```bash
python main.py
```

You will be prompted to confirm before sending:

```
Recipients loaded: 5000
Subject: Spring Sale is here!
Send to all 500 recipients? (yes/no): yes
```

To retry only failed recipients from a previous run:

```bash
python main.py --retry-failed
```

---

## 📊 Output

After the run completes, you will see a summary in the terminal:

```
==================================
   EMAIL DELIVERY SUMMARY
==================================
Total recipients : 5000
Sent             : 4873
Failed           : 127
Success rate     : 97.5%
Duration         : 4m 12s
==================================
Log saved to     : output/sent_log.csv
Failed saved to  : output/failed_recipients.csv
==================================
```

### sent_log.csv columns

| timestamp | recipient | subject | status | error |
|---|---|---|---|---|
| 2025-03-24 09:00:03 | alice@example.com | Spring Sale! | SENT | |
| 2025-03-24 09:00:05 | bad@@email.net | Spring Sale! | FAILED | SMTPRecipientsRefused |

---


## 🛡️ Error Handling

| Error | What happens |
|---|---|
| Invalid email address | Logged as FAILED, skipped |
| SMTP timeout | Retried up to 3 times |
| Auth failure | Script stops immediately with a clear message |
| Missing CSV column | Script stops immediately with a clear message |

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

> Built with Python · smtplib · Jinja2 · python-dotenv