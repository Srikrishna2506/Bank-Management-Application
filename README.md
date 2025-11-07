# 🏦 FLM BANK — Python Console Application

FLM Bank is a Python-based command-line banking system that offers secure user registration, OTP-based verification, and core banking functionalities such as deposits, withdrawals, and fund transfers.
It seamlessly integrates with a MySQL database for data management and Gmail’s email service for OTP delivery, ensuring both security and reliability.

---

## ✨ Features

- 🧾 **User Registration** with validation  
- ✉️ **Email OTP Verification** during signup  
- 🔐 **Login & Forgot Password** options  
- 💰 **Banking Operations:**
  - Display Balance  
  - Deposit Money  
  - Withdraw Money  
  - Transfer Funds  
  - Transaction History  
- 🧱 **Database Integration** (MySQL)
- 🎨 **ASCII Banner** & **Exit Banner**

---

## 🧠 Application Flow

1. **App Start:**  
   Displays the **FLM Bank banner** using `bannerPrinting()` from `banner_printing.py`.

2. **Main Menu Options:**  
   - Register  
   - Login  
   - Forgot Password  
   - Exit  

3. **Registration:**  
   - Collects user info → validates using `validations.py`.  
   - Stores data in DB using `insert_data()` from `db_operations.py`.  
   - Sends OTP for verification via `mailOtpVerification()`.

4. **Login:**  
   - Authenticates user credentials.  
   - On success, provides access to banking services.

5. **Banking Services:**  
   - `displayBalance()`  
   - `depositMoney()`  
   - `withdrawlMoney()`  
   - `transferMoney()`  
   - `transactionHistory()`

6. **Forgot Password:**  
   - Sends OTP and resets password securely.

7. **Exit:**  
   - Displays exit banner via `exit_banner_printing()`.

---

## 🗂️ Project Structure

                      
           FLM_Banking/
           │
           ├── com/
           │   ├── app.py                 # Main application entry point
           │   ├── constants.py           # Email credentials and DB config
           │   │
           │   ├── repo/
           │   │   └── db_operations.py   # DB insert, fetch, update, delete
           │   │
           │   ├── service/
           │   │   ├── user_service.py    # Create account, login, forgot password
           │   │   ├── banking_service.py # Deposit, withdraw, transfer, history
           │   │   ├── banner_printing.py # Banner and exit banner display
           │   │   ├── mail_operations.py # OTP and email service
           │   │   └── validations.py     # Input validations
           │   │
           │   └── util/
           │       └── user_security.py   # Password hashing, login tracking
           │
           ├── Banner.txt                 # Welcome banner text
           ├── Exit_Banner.txt            # Exit banner text
           └── README.md                  # Documentation


---

## ⚙️ Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install mysql-connector-python


2. Set up Database

       Create a MySQL database named flm_bms and run the provided SQL scripts to create tables.

3. Update Email Credentials
  In constants.py, set:

       SENDERMAIL = "yourmail@gmail.com"
  
       MAILPASS = "your_app_password"


4. Run the App

       python com/app.py

---

## 🛠️ Technologies Used

| Category        | Technology Used |
|-----------------|-----------------|
| **Language**    | Python 3 |
| **Database**    | MySQL |
| **Libraries**   | `mysql-connector`, `smtplib`, `hashlib`, `datetime`, `random` |
| **IDE**         | PyCharm / VS Code |

---

💡 Future Enhancements

Delete or update user details

Unlock blocked accounts

Email mini statements

Admin control panel

---

👨‍💻 Author

Srikrishna Laxetti (Kittu)

📧 kittuak25@gmail.com

📍 Hyderabad, India

---

⭐ FLM Bank – A simple and secure console banking experience built with Python.
