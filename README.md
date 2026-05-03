# Email Sender Automation 📧

[![PyPI version](https://img.shields.io/pypi/v/email-sender-automation.svg)](https://pypi.org/project/email-sender-automation/)
[![Python version](https://img.shields.io/pypi/pyversions/email-sender-automation.svg)](https://pypi.org/project/email-sender-automation/)
[![License](https://img.shields.io/pypi/l/email-sender-automation.svg)](https://pypi.org/project/email-sender-automation/)
[![Downloads](https://img.shields.io/pypi/dm/email-sender-automation.svg)](https://pypi.org/project/email-sender-automation/)

A beginner-friendly tool to easily send automated, personalized bulk emails using your Gmail account.

## ✨ Features

- **Personalized Emails**: Send custom emails (e.g., "Hi Alisa", "Hi Bobin") using a simple CSV file.
- **Beautiful HTML Templates**: Write emails in HTML, keeping them looking professional.
- **Automatic Retries**: If an email fails to send, the tool waits and tries again up to 3 times.
- **Delivery Tracking**: Keeps a neat log of every successful and failed email.
- **Retry Failed**: A single command to re-send only to people who failed the first time.
- **Safe & Secure**: Uses hidden environment variables so your password is never exposed.

## 📂 Project Structure

When you set up this tool, your project folder will look like this:

```text
email-sender-automation/
├── .env                      # 🔐 Your secret Gmail credentials (never share this!)
├── data/
│   ├── contacts.csv          # 👥 The list of people RECEIVING your emails
│   └── template.html         # 📝 The email design and message
└── output/
    ├── sent_log.csv          # ✅ Automatically created list of successful sends
    └── failed_recipients.csv # ❌ Automatically created list of failed sends
```

## 🚀 Step-by-Step Setup Guide

Follow these steps exactly to get your automated emailer running from scratch!

### Step 1: Install the Package
Open your terminal (or command prompt) and run this command:
```bash
pip install email-sender-automation
```

### Step 2: Create Your Folders
Create a new folder for your email project. Inside that folder, create two sub-folders named `data` and `output`.

```bash
mkdir my-email-project
cd my-email-project
mkdir data output
```

### Step 3: Set up your `.env` File
This file holds the credentials for the **SENDER** (you). Create a file named exactly `.env` (don't forget the dot at the beginning!) in your main folder.

Add this inside your `.env` file:
```env
# The email address that is SENDING the emails (Your Gmail)
EMAIL_USER=your_actual_email@gmail.com

# Your Gmail App Password (NOT your normal login password. See the guide below!)
EMAIL_PASS=xxxx xxxx xxxx xxxx
```

### Step 4: Create your `contacts.csv`
This file contains the **RECEIVERS** (the people getting the emails). Create a file named `contacts.csv` inside your `data` folder.

Add this exact text inside `data/contacts.csv`:
```csv
name,email,company
Alice,alice@example.com,Acme Corp
Bob,bob@example.com,Globex
```
*Note: The `email` column here is who receives the email.*

### Step 5: Create your `template.html`
This is what your email will look like. Create a file named `template.html` inside your `data` folder.

Add this exact text inside `data/template.html`:
```html
<!DOCTYPE html>
<html>
<body>
    <h2>Hello {{ name }}!</h2>
    <p>This is an automated message to say hi to you at <strong>{{ company }}</strong>.</p>
    <p>Best regards,<br>The Automation Team</p>
</body>
</html>
```

### Step 6: Run the Script!
Now you are ready to send! Open your terminal, make sure you are in your project folder, and try these commands:

**Command A: Send a quick test to yourself (Default)**
```bash
email-sender
```

**Command B: Send to everyone in your CSV (Bulk Send)**
```bash
email-sender --bulk
```

**Command C: Retry sending to anyone who failed**
```bash
email-sender --retry-failed
```

### Step 7: Check your Output
After running the bulk send, look inside your `output` folder. You will see new files:
- Open `output/sent_log.csv` to see exactly who successfully received your email and when.

---

## 🧑‍🏫 Sender vs Receiver: Explained

The biggest point of confusion is mixing up who is sending and who is receiving. Let's make it crystal clear:

| Role | Who is it? | Where does it go? | What does it do? |
|---|---|---|---|
| 📤 **SENDER** | **You** (Your Gmail Account) | In the **`.env`** file | This account logs into Gmail and pushes the emails out. |
| 📥 **RECEIVER** | **Your Contacts** (Customers, friends) | In the **`contacts.csv`** file | These are the addresses that show up in the "To:" line of the email. |

**Rule of Thumb:** Your own email goes in `.env`. Everyone else's email goes in `contacts.csv`.

---

## 🔑 Gmail App Password Setup Guide

Google does not let scripts log in with your normal password. You MUST create a special "App Password".

1. Go to your [Google Account Manage page](https://myaccount.google.com/).
2. Click on **Security** on the left menu.
3. Under "How you sign in to Google", ensure **2-Step Verification** is turned **ON**. (You cannot make an App Password without this).
4. Click on **2-Step Verification**, scroll to the very bottom, and click **App passwords**.
5. Give it a name (like "Python Emailer") and click **Create**.
6. A box will pop up with a 16-letter password (e.g., `abcd efgh ijkl mnop`).
7. Copy that 16-letter password, remove the spaces, and paste it into your `.env` file as your `EMAIL_PASS`.

---

## ⚙️ Configuration Variables

These are the settings you can put in your `.env` file:

| Variable | Description | Default | Example |
|---|---|---|---|
| `EMAIL_USER` | **(Required)** Your Gmail address used to send emails. | None | `you@gmail.com` |
| `EMAIL_PASS` | **(Required)** Your 16-character Gmail App Password. | None | `abcdefghijklmnop` |

---

## 💻 CLI Usage

The tool is run from the command line by typing `email-sender`. Here are the flags you can use:

| Command | What it does | Example |
|---|---|---|
| `email-sender` | Sends a single test email to your own `EMAIL_USER` address. Good for checking if your password works. | `email-sender` |
| `email-sender --bulk` | Reads `data/contacts.csv` and sends a personalized email to every row. | `email-sender --bulk` |
| `email-sender --retry-failed` | Reads `output/failed_recipients.csv` and tries to resend emails only to those who failed. | `email-sender --retry-failed` |

---

## 📁 Output Files Explained

When you run the tool, it automatically creates logs in the `output/` folder so you never lose track.

- **`sent_log.csv`**: A receipt of success. Contains the timestamp, the email address, and the subject of every email that successfully left your outbox.
- **`failed_recipients.csv`**: A list of problems. If an email address was typed wrong, or your internet dropped, the email goes here along with the exact error message.

---

## 🚨 Error Handling

Things go wrong! Here is how the tool handles them:

| Error | What Happens | Where to look |
|---|---|---|
| **No Internet Connection** | Tool waits a few seconds (exponential back-off) and tries 3 times. If it still fails, it saves the email to the failed list. | `output/failed_recipients.csv` |
| **Wrong App Password** | The program crashes immediately and tells you the login failed. No emails are sent. | Terminal screen |
| **Missing `.env` file** | The program stops and tells you to create the file. | Terminal screen |
| **Missing `{{ name }}` in CSV** | Jinja2 will just leave the space blank. "Hello {{ name }}" becomes "Hello ". | Recipient's Inbox |

---

## ❓ FAQ (Frequently Asked Questions)

**1. Is it safe to put my password in the `.env` file?**
Yes, as long as you don't share the `.env` file with anyone or upload it to the internet (like GitHub). The `.env` file is meant to be a local secret.

**2. Can I use Yahoo or Outlook instead of Gmail?**
Currently, this package is hardcoded to use `smtp.gmail.com` on port `587`. It is designed specifically for Gmail.

**3. What happens if the script crashes halfway through sending?**
Check your `output/sent_log.csv`. Anyone on that list got the email. You can remove them from your `contacts.csv`, and run the script again.

**4. Can I send attachments (like PDFs)?**
This version of the tool only supports sending text and HTML emails. Attachments are not currently supported.

**5. I'm getting a "ModuleNotFoundError: No module named 'dotenv'". What do I do?**
This means the package isn't installed properly in your current environment. Run `pip install email-sender-automation` again to make sure all dependencies download.

---

## 📜 License

This project is licensed under the MIT License. Feel free to use it, modify it, and share it!
