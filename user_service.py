from random import randint
import time
from FLM_Banking.com.service.validations import *
from FLM_Banking.com.service.mail_operations import *
from FLM_Banking.com.service.user_security import *

class CreateAccount:
    def accountCreation(self):

        # collecting user details
        self.fname = input("Please Enter your First Name: ")
        self.lname = input("Please Enter your Last Name: ")
        self.name = self.fname + self.lname
        self.gender = genderValidation()
        self.dob = dateValidation()
        self.mobileNo = mobileNumValidation()
        self.aadhar = input("Please Enter your 12 digit AAdhar Number: ")
        self.email = emailValidation()
        self.salt,self.password = passwordValidation()
        self.initialDeposit = int(input("Enter Initial deposit (>1000): "))
        #self.balance = self.initialDeposit()

        print()
        print("[+] OTP Verification Process initiated")
        print()

        # code to verify email through OTP and checking whether account number created is unique or not
        if mailOtpVerification(self.email):
            print("[+] OTP Verified Successfully...")
            print()
            while 1:
                # generating a new random account number
                self.accountNumber = randint(100000, 999999)
                print("[+] Account Created, Your Account Number is: " + str(self.accountNumber))
                print()

                # checking whether generated account number is unique or not, if not regenerate account number
                if uniqueAccNum(self.accountNumber):
                    break
                else:
                    continue

        # inserting user details into database, table flm_users
        insert_data('flm_users', first_name=self.fname, last_name=self.lname, email=self.email, dob=self.dob,
                    salt=self.salt, password=self.password)


        # fetching userId of the new user created
        self.userId = fetch_data('flm_users', email=self.email)

        # inserting account info into database, table flm_accounts for new user created
        insert_data('flm_accounts', user_id=self.userId[0][0], account_number=self.accountNumber, balance=self.initialDeposit, is_active=True)

        return



def login(user_mail):

    while True:

        # checking whether user_mail exist or not in flm_users
        if user_mail in fetch_column_data('flm_users', 'email'):
            user_password = input("Password: ")
            print()

            # fetching user data from db using user_mail
            db_data = fetch_data('flm_users', email=user_mail)

            # extracting user data
            failedLoginAttemps = db_data[0][7]
            db_salt = db_data[0][5]
            db_password = db_data[0][6]

            if failedLoginAttemps > MAX_LOGIN_ATTEMPTS:
                print("[-] Maximum Login Attempts Reached.. Account Locked...")
                print()

                # resetting failedLoginAttempts to 0 after 30 seconds
                # if not is_locked:
                #     reset_variable_after_30_seconds(user_mail)
                # else:
                #     is_locked = True

                #time.sleep(30)
                return False
                #code to reset failedLoginAttempts to 0 after certain time
            else:

                # hashing user entered password with salt from database
                hashed_user_password = hash_password_with_salt(db_salt,user_password)


                # if not is_locked:
                    # checking whether user entered password is same as database password
                if hashed_user_password == db_password:

                    # update failedcountattempts to 0 in flm_users
                    update_data('flm_users', values={'failedcountattempts': 0}, conditions={'email': user_mail})

                    # extracting last login data
                    last_login_date = db_data[0][8]
                    print("[+] last login date and time: " + str(last_login_date))
                    print()

                    # updating last_login_time in flm_users to CURRENT TIME
                    update_last_login_by_email(user_mail)
                    print("[+] Login Successful.. Please select operation to perform from below menu...")
                    print()
                    return True
                else:
                    failedLoginAttemps += 1
                    update_data('flm_users', values={'failedcountattempts': failedLoginAttemps}, conditions={'email': user_mail})
                    return False
                # else:
                #     print("[-] Account is locked.. Please try after some time...")
                #     print()
                #     return False

        else:
            print("[-] Invalid Mail id, Please try again..")
            return False



def forgotPassword():

    # taking user_mail id as input
    user_mail = input("Enter Mail Id: ")
    try:

        # fetching user data row from flm_users table based on user_mail
        db_data = fetch_data('flm_users', email=user_mail)

        # extracting user dob from user data row fetched
        db_dob = db_data[0][4]

        # taking dob from user for further validation
        user_dob = dateValidation()

        # checking database_dob with user_dob entered
        if user_dob == str(db_dob):

            # verifying again with OTP to change password
            if mailOtpVerification(user_mail):

                # allowing user again to create new password
                updated_salt,updated_password = passwordValidation()

                # updating new password, salt into user database in flm_users table based on user_mail
                update_data('flm_users', values={'password': updated_password,'salt': updated_salt}, conditions={'email': user_mail})

                return True
            else:
                print("[-] OTP Verification failed, Please try again...")
                return False
        else:
            print("[-] DOB Verification failed, Please try again...")
            return False

    except:
        return False

