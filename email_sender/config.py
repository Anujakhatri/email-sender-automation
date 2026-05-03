import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

if not EMAIL_USER or not EMAIL_PASS:
    raise ValueError("EMAIL_USER and EMAIL_PASS must be set in .env file")

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_HTML = BASE_DIR / "data" / "template.html"
