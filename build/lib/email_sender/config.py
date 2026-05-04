import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

# Automatically search for .env in current and parent directories
load_dotenv(find_dotenv(usecwd=True))

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

if not EMAIL_USER or not EMAIL_PASS:
    raise ValueError("EMAIL_USER and EMAIL_PASS must be set in .env file")

BASE_DIR = Path.cwd()
TEMPLATE_HTML = BASE_DIR / "data" / "template.html"
