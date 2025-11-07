import hashlib
import secrets
import time
from FLM_Banking.com.repo.db_operations import *


def hash_password_with_salt(salt,password):
    # Generate a random salt
    #salt = secrets.token_hex(16)  # 16 bytes of random data

    # Concatenate the salt and password
    salted_password = str(salt) + password

    # Hash the salted password using SHA-256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

    # Return the salt and hashed password as a tuple
    return hashed_password




# def reset_variable_after_30_seconds(user_email):
#     # Set the initial time
#     start_time = time.time()
#     while True:
#         # Check the current time
#         current_time = time.time()
#
#         # Calculate the elapsed time
#         elapsed_time = current_time - start_time
#
#         if elapsed_time >= 30:  # 30seconds
#             # Reset the variable to 0 here
#             update_data('flm_users', values={'failedcountattempts': 0}, conditions={'email': user_email})
#             print("[+] Hurray... Account is Unlocked... Try Logging in Now...")
#             print()
#             break


# # Example usage:
# password = "my_secure_password"
# salt, hashed_password = hash_password_with_salt(password)
#
# print("Salt:", salt)
# print("Hashed Password:", hashed_password)
