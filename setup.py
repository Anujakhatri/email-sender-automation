from setuptools import setup, find_packages

setup(
    name="email_sender-automation",
    version="0.1.0",
    author="Anuja Khatri",
    author_email="khatrianuja20@gmail.com",
    description="email-sender-automation tools built with python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Anujakhatri/email-sender-automation",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)