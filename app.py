from FLM_Banking.com.service.user_service import *
from FLM_Banking.com.service.banner_printing import *
from FLM_Banking.com.service.banking_service import *
import time

# code to print FLB Bank banner

def bannerPrinting():
    print("===================================")
    print("        Welcome to FLM Bank        ")
    print("===================================")

def exit_banner_printing():
    print("===================================")
    print("      Exiting from FLM Bank        ")
    print("===================================")

try:
    bannerPrinting()
except:
    print("[-] Banner Loading Failed...")
    quit()

# displaying choice table
while True:
    print()
    print("Enter 1 to Register")
    print("Enter 2 to Login")
    print("Enter 3 to Forgot Password")
    print("Enter 4 to Exit")
    print()

    userChoice = int(input())

    if userChoice == 1:
        print("[+] Account Creation in process....\n")
        time.sleep(2)

        # Function Responsible to create a account is called.
        ca = CreateAccount()
        ca.accountCreation()

        # Once Account created, CreateAccount() completes execution controller should repeat with start menu options again
        continue


    elif userChoice == 2:

        # accessing existing account
        print()

        # user providing password for login/authentication
        user_mail = input("Username(Email): ")

        # login/authentication initiated
        if login(user_mail) == False:
            print("[-] Login Failed....")
            print()
            continue
        else:
            while True:
                print("[+] Please select operation to perform from below menu...")
                print()
                print("Enter 1 to Display Balance.")
                print('Enter 2 to Deposit Money.')
                print("Enter 3 to Withdraw Money.")
                print("Enter 4 to Transfer Money.")
                print("Enter 5 to Print Transaction History.")
                print("Enter 6 to Log Out.")
                print()

                userChoice = int(input())

                if userChoice == 1:
                    print()

                    # calling function that display balance
                    if displayBalance(user_mail):
                        pass
                    else:
                        print("[-] Problem in Displaying Balance... ")
                        print()


                elif userChoice == 2:
                    print()
                    try:
                        depositAmount = int(input("[+] Enter Amount to Deposit: "))
                        print()
                    except:
                        print("[-] Enter Valid Amount..")
                        print()
                        continue

                    # calling function that is responsible to deposit money
                    # user_mail to identify user, depositAmount to specify amount to bee deposited
                    if depositMoney(user_mail,depositAmount):
                        print("[+] Deposit Successful...")
                        print()
                        continue
                    else:
                        print("[-] Deposit Unsuccessful...")
                        print()
                        continue


                elif userChoice == 3:
                    print()
                    try:
                        withdrawlAmount = int(input("[+] Enter Withdrawl Amont: "))
                        print()
                    except:
                        print("[-] Enter Valid Amount..")
                        print()
                        continue

                    if withdrawlMoney(user_mail,withdrawlAmount):
                        print('[+] Money withdrawl Successfull..')
                        print()
                        continue
                    else:
                        print("[-] Withdrawl Unsuccessfull..")
                        print()
                        continue


                elif userChoice == 4:
                    print()
                    try:
                        transferAmount = int(input("Enter Amount to be Transfered: "))
                        print()
                    except:
                        print("[-] Enter Valid Amount..")
                        continue

                    if transferMoney(user_mail,transferAmount):
                        print("[+] Money Transfer Successfull..")
                        print()
                        continue
                    else:
                        print("[-] Money Transfer Unsuccessfull..")
                        print()
                        continue


                elif userChoice == 5:
                    print()
                    if transactionHistory(user_mail):
                        continue
                    else:
                        print("[-] Printing Transaction History Failed...")
                        print()
                        continue

                # logout functionality
                elif userChoice == 6:
                    print("[-] Logout Successfull...")
                    print()
                    break

    elif userChoice == 3:
        if forgotPassword():
            print('[+] Password Reset Succesfull.. ')
            print()
            continue
        else:
            print('[+] Password Reset UnSuccesfull.. ')
            print()
            continue


    elif userChoice == 4:
        exit_banner_printing()
        print()
        print("[+] Thank You for using FLM Bank, See you soon..")
        quit()


#done