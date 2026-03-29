import os, subprocess
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("TWINE_USERNAME")
password = os.getenv("TWINE_PASSWORD")

subprocess.run("rm -rf dist build *.egg-info", shell=True)
subprocess.run("python -m build", shell=True)
subprocess.run(f"twine upload -u {username} -p {password} dist/* --verbose", shell=True)