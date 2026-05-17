
# Gmail To user


import smtplib
import mailCredential
import random


def sendMail(receiver_address):
    sender_address = mailCredential.getSenderID()
    sender_pass = mailCredential.getSenderPassword()

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login(sender_address, sender_pass)
    
    # message to be sent
    # message = "Message_you_need_to_send"

    otp = str(random.randint(100000,999999))

    subject = "This Mail Is From Shopping Cart"
    content = "Dear User,\n\nYour OTP is :- " + otp + "." + "\n\nThanks & Regards"
    
    message = 'Subject: {}\n\n{}'.format(subject, content)

    # sending the mail
    s.sendmail(mailCredential.getSenderID(), receiver_address , message)
    # terminating the session
    s.quit()
    return otp