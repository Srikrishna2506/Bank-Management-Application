
from FLM_Banking.com.repo.db_operations import *

# function to fetch userId based on user_email
def fetch_userID(user_mail):

    # fetching entire row based on email from flm_users
    db_data_users = fetch_data('flm_users', email=user_mail)
    try:
        # fetching userId variable from entire row
        userId = db_data_users[0][0]
        return userId

    except:
        return False


def displayBalance(user_mail):

    #fetching userId based on user_mail from flm_users table
    userId = fetch_userID(user_mail)

    if userId:
        db_data_accounts = fetch_data('flm_accounts', user_id=userId)
        print("[+] Account Balance: " + str(db_data_accounts[0][3]))
        print()
        return True

    else:
        return False


def depositMoney(user_mail,depositAmount):

    # fetching userId based on user_mail from flm_users table
    userId = fetch_userID(user_mail)

    if userId:
        try:
            # fetching entire row of flm_accounts table based on userId
            db_data_accounts = fetch_data('flm_accounts', user_id=userId)

            # extracting and updating balance variable from entire row
            balance = db_data_accounts[0][3] + depositAmount

            # updating balance variable in database, flm_accounts table using userId
            update_data('flm_accounts', values={'balance': balance}, conditions={'user_id': userId})
            displayBalance(user_mail)

            return True

        except:

            return False
    else:

        return False

def withdrawlMoney(user_mail,withdrawlMoney):

    # fetching userId based on user_mail from flm_users table
    userId = fetch_userID(user_mail)

    if userId:

        # fetching entire row of flm_accounts table based on userId
        db_data_accounts = fetch_data('flm_accounts', user_id=userId)

        # extracting user balance from entire row data
        balance = db_data_accounts[0][3]

        # function to check whether user balance is greater than withdrawlamount
        if balance > withdrawlMoney:
            balance = balance - withdrawlMoney

            # updating new user balance into database
            update_data('flm_accounts', values={'balance': balance}, conditions={'user_id': userId})
            displayBalance(user_mail)
            return True

        else:
            print("[-] Insufficient Funds...")
            print()
            return False

    else:
        return False


def transferMoney(user_mail,transferAmount):

    # fetching senderUserId based on user_mail from flm_users table
    senderUserId = fetch_userID(user_mail)

    # fetching account information from senderUserId from flm_accounts table
    senderAccountDetails = fetch_data('flm_accounts', user_id=senderUserId)

    # extracting senderDetails from flm_accounts table
    senderBalance = senderAccountDetails[0][3]
    senderAccountId = senderAccountDetails[0][0]
    senderAccountNumber = senderAccountDetails[0][2]

    # checking whether senderBalance is greater than amount to be transferred
    if senderBalance > transferAmount:

        # receiver accountId
        receiverAccountId = int(input("Enter Recepients Account Id: "))
        #account_ids = fetch_column_data('flm_accounts', 'account_id')

        # checking whether receiver account does exist or not
        if receiverAccountId in fetch_column_data('flm_accounts', 'account_id'):

            # performing update operations on sender account balance
            UptSenderBalance = senderBalance - transferAmount

            # updating new sender account info into flm_accounts database
            update_data('flm_accounts', values={'balance': UptSenderBalance}, conditions={'user_id': senderUserId})
            displayBalance(user_mail)

            # fetching receiver account info from flm_accounts
            receiver_db_data = fetch_data('flm_accounts', account_id=receiverAccountId)

            # extracting receiver data
            receiverUserId = receiver_db_data[0][1]
            receiverAccountNumber = receiver_db_data[0][2]

            # performing update operations on receiver account balance
            receiverBalance = receiver_db_data[0][3] + transferAmount

            # updating receiver account info into database
            update_data('flm_accounts', values={'balance': receiverBalance}, conditions={'account_id': receiverAccountId})



            # inserting transaction details into flm_transactions table (sender side)
            insert_data('flm_transactions', user_id=senderUserId, account_id=senderAccountId, amount=transferAmount, from_account=senderAccountNumber,
                        to_account=receiverAccountNumber, trans_type='db')


            # inserting transaction details into flm_transactions table (sender side)
            insert_data('flm_transactions', user_id=receiverUserId, account_id=receiverAccountId, amount=transferAmount,
                        from_account=senderAccountNumber,
                        to_account=receiverAccountNumber,trans_type='cd')

            return True

        else:
            print("[-] Receiver Account Do not exist..")
            print()
            return False

    else:
        print("[-] Insufficient Balance..")
        print()
        return False

def transactionHistory(user_email):
    try:
        # Connect to the MySQL database
        conn = db_connect()

        # Create a cursor to execute SQL queries
        cursor = conn.cursor()

        # Query to retrieve transaction history based on user email
        query = """
                SELECT flm_users.first_name, flm_users.last_name, flm_accounts.account_number, flm_transactions.amount, flm_transactions.from_account, flm_transactions.to_account, flm_transactions.trans_date, flm_transactions.trans_type
                FROM flm_users
                INNER JOIN flm_transactions ON flm_users.user_id = flm_transactions.user_id
                INNER JOIN flm_accounts ON flm_transactions.account_id = flm_accounts.account_id
                WHERE flm_users.email = %s
            """

        # Execute the query with the provided user_email
        cursor.execute(query, (user_email,))

        # Fetch and print the transaction history
        print("Transaction History for User:", user_email)
        print("{:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<10}".format("First Name", "Last Name",
                                                                               "Account Number", "Amount",
                                                                               "From Account", "To Account", "Date",
                                                                               "Trans Type"))
        for row in cursor.fetchall():
            first_name, last_name, account_number, amount, from_account, to_account, trans_date, trans_type = row
            print(
                "{:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<10}".format(first_name, last_name, account_number,
                                                                                 amount, from_account, to_account, str(trans_date),
                                                                                 trans_type))

        print()
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return True

    except mysql.connector.Error as e:
        #
        # baprint("Error:", e)
        return False




