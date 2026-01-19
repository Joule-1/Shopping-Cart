import otpGenerator
import smtplib

def emailSender(recipient_email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('
    # Simulate sending email by printing to console
    print(f"Sending OTP {otpGenerator.otpGenerator()} to email: {recipient_email}")
``