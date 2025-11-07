import re
from random import randint
import hashlib
from FLM_Banking.com.repo.db_operations import *

def genderValidation():
    while 1:

        # taking gender value from user and converting it into lowercase
        gender = input("Please Enter your Gender [m/f/o]: ").lower()
        print()

        # checking entered gender is in specified one or not
        if gender in ['m','f','o']:
            return gender
        else:
            print("[-] Please Enter Specified Gender Types only...")
            print()
            continue


def mobileNumValidation():
    while -1:

        # taking gender value from user and converting it into lowercase
        mobileNo = input("Please Enter Your Mobile Number: ")
        print()

        # regex pattern to check whether string has 10 numbers or not
        pattern = r'^\d{10}$'

        # Use the re.match function to check if the number matches the pattern
        if re.match(pattern, mobileNo):
            return mobileNo
        else:
            print("[-] Please Enter Valid Mobile Number: ")
            print()
            continue

# def uniqueEmail(email):
#     try:
#         conn = db_connect()
#         cursor = conn.cursor()
#         # Execute a query to check if the email already exists
#         query = "SELECT COUNT(*) FROM flm_users WHERE email = %s"
#         cursor.execute(query, (email,))
#         # print(cursor.fetchall())
#         # print(cursor.fetchone())
#         # print(cursor.fetchone()[0])
#         result = cursor.fetchone()[0]
#         conn.close()
#
#         # If result is 0, the email is unique; otherwise, it's not
#         if result == 0:
#             return True
#         else:
#             return False
#
#     except Exception as err:
#         print("Something Went Wrong: ", err)
#         return False

def uniqueEmail(emailId):

    # checking emailId is unique or not
    # by fetching email column from flm_users table
    if emailId in fetch_column_data('flm_users','email'):
        return False
    else:
        return True

# def uniqueAccNum(AccNum):
#     try:
#         conn = db_connect()
#         cursor = conn.cursor()
#         # Execute a query to check if the email already exists
#         query = "SELECT COUNT(*) FROM flm_accounts WHERE account_number = %s"
#         cursor.execute(query, (AccNum,))
#         # print(cursor.fetchall())
#         # print(cursor.fetchone())
#         # print(cursor.fetchone()[0])
#         result = cursor.fetchone()[0]
#         conn.close()
#
#         # If result is 0, the email is unique; otherwise, it's not
#         if result == 0:
#             return True
#         else:
#             return False
#
#     except Exception as err:
#         print("Something Went Wrong: ", err)
#         return False

def uniqueAccNum(AccNum):

    # checking AccNum is unique or not
    # by fetching account_number column in flm_accounts
    if AccNum in fetch_column_data('flm_accounts','account_number'):
        return False
    else:
        return True


def emailValidation():
    while 1:

        # collecting user email id
        email = input("Please Enter your Gmail address: ")
        print()
        #isUnique = uniqueEmail(email)

        # pattern used to check whether entered email is valid or not
        pattern = r'^\S+@\S+\.\S+$'

        # Use the re.match() function to check if the email matches the pattern
        if re.match(pattern, email):

            # check whether entered email is unique or not
            if uniqueEmail(email):
                return email
            else:
                print("[-] This Email is Taken Please, Provide another Email Address: ")
                print()
                continue
        else:
            print("[-] Please Enter Valid Gmail Address: ")
            print()
            continue


def passwordValidation():
    while -10:
        # update for password strength
        # salt = secrets.token_hex(16)  # 16 bytes of random data

        # generating salt randomly
        salt = randint(00000,99999)

        # taking password from user
        password = input("Please type your Password: ")

        # taking confirm password from user
        confirmPassword = input("Please Re-type your Password: ")
        print()

        # comparing both password and confirm password, if same proceed
        if password == confirmPassword:

            # adding salt with password
            password = str(salt) + password

            # hashing password to maintain security
            password = hashlib.sha256(password.encode()).hexdigest()
            return salt, password
        else:
            print("[-] Password and Confirm Password do no match try again....")
            print()
            continue

def dateValidation():
    while 6:

        # check min,max dates to avoid future dates for dob
        # collecting dob from users in specified format
        dob = input("Please Enter your Date of Birth in DD/MM/YYYY Format: ")
        print()

        # pattern to check whether entered dob is matching specified format
        pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'

        # checking entered dob with pattern
        if re.match(pattern, dob):
            return dob
        else:
            print("[-] Date of Birth do no match with expected Pattern try again....")
            print()
            continue



# email = emailValidation()
# print(email)


# AccNum = input("Enter account num: ")
# if uniqueAccNum(AccNum):
#     print("Unique")
# else:
#     print("not Unique")
