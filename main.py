from email_sender.sender import send_email

if __name__ == "__main__":
    subject = "Test Email"
    body = "It works!"

    # Send to yourself
    send_email(subject, body)

    # Send to another user
    send_email(subject, body, recipients="indukc261@gmail.com")

    # we can send to multiple recipients like this
    # send_email(subject, body, recipients=["friend1@gmail.com", "friend2@gmail.com"])