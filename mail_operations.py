import time

import smtplib
from random import randint
from FLM_Banking.com.service.constants import *

# function that generates random number
def otp_gen():
    otp = randint(100000, 999999)
    return otp


# function that sends mail and verifies OTP
def mailOtpVerification(email):

    # senderMail = SENDERMAIL
    # password = MAILPASS

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(SENDERMAIL, MAILPASS)

    otp = otp_gen()

    server.sendmail(SENDERMAIL, email,
                    "Welcome, to FLM Bank, Trust Above all.\n" + "your OTP number is :" + str(otp))

    print("otp sent to: " + email)
    server.quit()
    print()
    user_otp = int(input("please Enter OTP to continue: "))

    if user_otp == otp:
        # print("OTP Verified")
        return True
    else:
        # print("OTP Not Verified")
        return False



# email = input("Enter email:")
#mailOtpVerification('gourusaikumar789@gmail.com')
