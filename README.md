# Banking-System
🔁 Startup Process
It counts how many users already exist by reading the BankSystem.csv file.
Initializes a global counter that acts as the next account number.


🧾 Main Menu Options
The program repeatedly shows a menu with:

1 - Account Creation

2 - Log In

exit - Exit the Program

✅ 1. Account Creation
User enters name, password, and an initial deposit (must be at least $100).
A new .csv file is created per user (e.g., 5.csv) to log their transactions.
Data is also appended to BankSystem.csv with:\n
Account Number\n
Name
Password
Initial Deposit

🔐 2. Login System
User logs in with account number and password.
If credentials are correct, another menu appears with banking operations.

💰 Banking Options After Login
Once logged in, a user can:

Check Balance
-Reads the Ini_Deposit from BankSystem.csv.

Deposit Money
-Increases the user's balance.
-Updates the BankSystem.csv file.
-Logs the transaction in the user's personal .csv file.

Withdraw Money
-Decreases the user's balance if sufficient funds.
-Updates the same files as above.

Transfer Money
-Transfers money from one account to another:
-Deducts from sender
-Adds to receiver
-Both accounts' .csv files are updated

Passbook Print
-Reads and prints the user's transaction history from their .csv file.

Logout
-Exits back to the main menu.

❌ Exit
If the user types 'exit' at the main menu, the program ends.



