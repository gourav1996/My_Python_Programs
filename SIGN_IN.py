#SIGNIN PAGE
import random
import smtplib


def signin():
    otp=str(random.randint(100000,999999))
    email_id = str(input("Enter the Gmail Id::"))
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("senders@gmail.com ","password") # change according to ur gmail id and password
    server.sendmail("senders@gmail.com", email_id ,f"Your six digit OTP IS {otp}" )
        #email gets sent
    login_count=0
    login_attempts=3
    login_count=1
    login_attempts=4
    while login_count<login_attempts:
        login_count=login_count+1
        OTP_in=str(input("Enter 6 Digit Otp sent to you email id::"))
        if otp==OTP_in:
            print("Login Sucessfull")
            login_count=999
        else:
                print(f"Enter OTP AGAIN {login_count-1} attempts over max 3 ")
    if login_count>login_attempts:
        print("Rerun the program")


signin()

