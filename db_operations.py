import mysql.connector
from FLM_Banking.com.service.constants import *

def db_connect():
    try:
        # Establish database connection
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        return conn

    except mysql.connector.Error as err:
        print("Database Connection Error: ", err)
        print()



def insert_data(table_name, **kwargs):

    # establishing connection
    conn = db_connect()
    cursor = conn.cursor()

    try:

        # inserting data into flm_users table
        if table_name == "flm_users":
            sql = ("INSERT INTO flm_users (first_name, last_name, email, dob, salt, password) "
                   "VALUES (%(first_name)s, %(last_name)s, %(email)s, %(dob)s, %(salt)s, %(password)s)")

        # inserting data into flm_accounts table
        elif table_name == "flm_accounts":
            sql = ("INSERT INTO flm_accounts (user_id, account_number, balance, is_active) "
                   "VALUES (%(user_id)s, %(account_number)s, %(balance)s, %(is_active)s)")

        # inserting data into flm_transactions table
        elif table_name == "flm_transactions":
            sql = (
                "INSERT INTO flm_transactions (user_id, account_id, amount, from_account, to_account, trans_date, trans_type) "
                "VALUES (%(user_id)s, %(account_id)s, %(amount)s, %(from_account)s, %(to_account)s, NOW(), %(trans_type)s)")
        else:
            raise ValueError("Invalid table name")

        # executing insert query
        cursor.execute(sql, kwargs)
        conn.commit()
        return

    except mysql.connector.Error as err:
        print("Error in inserting data into database: ", err)
        conn.rollback() # Rollback in case of any error
        return

    finally:
        conn.commit()
        cursor.close()
        conn.close()




# Example usage:
# insert_data('flm_users', first_name='John', last_name='Doe', email='johndoe@example.com', dob='1990-01-01', salt='randomSalt123', password='hashedPassword456')
# insert_data('flm_accounts', user_id=1, account_number='1234567890', balance=1000.00, is_active=True)
# insert_data('flm_transactions', user_id=1, account_id=1, amount=200.00, from_account='1234567890', to_account='0987654321', data='2023-09-19', trans_type='db')


def fetch_data(table_name, **kwargs):
    # Establishing the connection
    conn = db_connect()
    cursor = conn.cursor()

    try:
        base_sql = f"SELECT * FROM {table_name}"

        # Construct WHERE clause based on provided filters
        filters = " AND ".join([f"{key}=%({key})s" for key in kwargs])

        if filters:
            sql = f"{base_sql} WHERE {filters}"
        else:
            sql = base_sql

        cursor.execute(sql, kwargs)

        # fetching all data based on where clause
        results = cursor.fetchall()
        #print(type(results))
        return results

    except mysql.connector.Error as err:
        print("Error:", err)
        return []

    finally:
        cursor.close()
        conn.close()

# Example usage:
# users = fetch_data('flm_users', email='johndoe@example.com')
# accounts = fetch_data('flm_accounts', user_id=1)
# transactions = fetch_data('flm_transactions', user_id=1, account_id=1)
# print(users, accounts, transactions)

def fetch_column_data(table_name, column_name):

    # Establishing the connection
    conn = db_connect()
    cursor = conn.cursor()

    try:
        sql = f"SELECT {column_name} FROM {table_name}"
        cursor.execute(sql)
        results = cursor.fetchall()
        return [row[0] for row in results]  # Extracting column values from the result rows

    except mysql.connector.Error as err:
        print("Error:", err)
        return False

    finally:
        cursor.close()
        conn.close()

# EXAMPLE USAGE
#
#user_emails = fetch_column_data('flm_accounts', 'account_number')
#print("User Emails:", user_emails)

def update_data(table_name, values, conditions):
    # Establishing  the connection
    conn = db_connect()
    cursor = conn.cursor()

    try:
        # Construct the SET clause for the UPDATE statement
        set_clause = ", ".join([f"{key}=%({key})s" for key in values])

        # Construct the WHERE clause for the UPDATE statement
        where_clause = " AND ".join([f"{key}=%({key})s" for key in conditions])

        sql = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"

        # Merge the values and conditions dictionaries for parameter substitution
        params = {**values, **conditions}

        cursor.execute(sql, params)
        conn.commit()

    except mysql.connector.Error as err:
        print("Error:", err)
        conn.rollback()  # Rollback in case of any error

    finally:
        conn.commit()
        cursor.close()
        conn.close()

# Example usage:
# update_data('flm_users', values={'last_name': 'Smith'}, conditions={'email': 'johndoe@example.com'})
# update_data('flm_accounts', values={'balance': 1200.00}, conditions={'account_number': '1234567890'})
# update_data('flm_transactions', values={'amount': 250.00}, conditions={'trans_id': 1})


def delete_data(table_name, conditions):
    # Establish the connection
    conn = db_connect()
    cursor = conn.cursor()

    try:
        # Construct the WHERE clause for the DELETE statement
        where_clause = " AND ".join([f"{key}=%({key})s" for key in conditions])

        sql = f"DELETE FROM {table_name} WHERE {where_clause}"

        cursor.execute(sql, conditions)
        conn.commit()

    except mysql.connector.Error as err:
        print("Error:", err)
        conn.rollback()  # Rollback in case of any error

    finally:
        cursor.close()
        conn.close()

# Example usage:
# delete_data('flm_users', conditions={'email': 'johndoe@example.com'})
# delete_data('flm_accounts', conditions={'account_number': '1234567890'})
# delete_data('flm_transactions', conditions={'trans_id': 1})

def update_last_login_by_email(user_mail):
    try:
        # Connect to the MySQL database
        conn = db_connect()

        # Create a cursor to execute SQL queries
        cursor = conn.cursor()

        # Update the lastlogin_date for the user with the given user_id
        update_query = """
            UPDATE flm_users
            SET lastlogin_date = NOW()
            WHERE email = %s
        """

        cursor.execute(update_query, (user_mail,))

        # Commit the changes to the database
        conn.commit()
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
        return

    except mysql.connector.Error as e:
        print("Error in updating last login time: ", e)
        return








# insert_data('flm_users', first_name='John', last_name='Doe', email='johndoe@example.com', dob='1990-01-01', salt='randomSalt123', password='hashedPassword456')
# insert_data('flm_accounts', user_id=1, account_number='1234567890', balance=1000.00, is_active=True)
# insert_data('flm_transactions', user_id=1, account_id=1, amount=200.00, from_account='1234567890', to_account='0987654321', date='2023-09-19', trans_type='db')
#accounts = fetch_data('flm_accounts', user_id=1)
#users = fetch_column_data('flm_users','email')
# accounts = fetch_data('flm_users', email='example@gmail.com')
# transactions = fetch_data('flm_transactions', user_id=1, account_id=1)
# print(accounts)
# print(accounts[0][8])
# print(type(accounts[0][8]))
# users = fetch_data('flm_users', email='johndoe@example.com')
#print(users)
# print(users[0][4])
# print(accounts)
# print(transactions)


# update_data('flm_users', values={'last_name': 'Smith'}, conditions={'email': 'johndoe@example.com'})
# update_data('flm_accounts', values={'balance': 1200.00}, conditions={'account_number': '1234567890'})
# update_data('flm_transactions', values={'amount': 250.00}, conditions={'trans_id': 1})