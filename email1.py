import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    # SMTP configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # For Gmail

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Attach the file
    if attachment_path:
        attachment = open(attachment_path, 'rb')

        # Create a MIMEBase object and set the necessary headers
        mime_base = MIMEBase('application', 'octet-stream')
        mime_base.set_payload(attachment.read())

        # Encode the attachment and add headers
        encoders.encode_base64(mime_base)
        mime_base.add_header('Content-Disposition', f'attachment; filename={attachment_path}')

        # Add the attachment to the email
        message.attach(mime_base)

    # Start the SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        # Login to your sender email account
        server.login(sender_email, sender_password)
        # Send the email
        server.send_message(message)

    print("Email sent successfully!")

# Example usage
# Example usage
sender_email = 'emailashutoshgaur@gmail.com'
sender_password = 'xxx'
receiver_email = 'emailashutoshgaur@gmail.com'
subject = 'Hello from Python!'
body = 'This is the body of the email.'
attachment_path = 'path_to_attachment_file.pdf'

send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)
