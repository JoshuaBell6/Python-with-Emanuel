# TASK: Create an ATM program.
"""
Rules:
    - Create a bank account object with following attributes:
        - account_holder (first name and last name)
        - balance (amount of money on the account)
    - Create an ATM object which holds accounts and has the following methods:
        - deposit (add money to the account)
        - withdraw (take money from the account)
        - get balance (gives you the info of how much money you have)
    [You are free to add more methods not specified here, but the ones above are mandatory]
    
    Menu:
        Account: Joshua Bell (EUR)
        1. Switch Accounts
        2. Create new account
        3. Deposit funds
        4. Withdraw funds
        5. Display current balance
        6. Change currency
        7. Leave

        SWITCH ACCOUNTS:
            - Display the list of accounts in a user-friendly manner
            - Alow user to change accounts
        CREATE NEW ACCOUNT:
            - Allow user to enter their first and last name
            - Every new account starts with the balance of 0 EUR
        DEPOSIT FUNDS:
            - Allow user to enter an amount they want to deposit
        WITHDRAW FUNDS:
            - Show the menu of funds available to withdraw (10, 20, 30, 50, 100, 150, 200, 300, 500) in a user-friendly manner
            - Users cannot withdraw the funds they don't have
        DISPLAY CURRENT BALANCE:
            - Display how much money the user has in a user-friendly manner
        CHANGE CURRENCY:
            - Allow user to change the fund currency between EUR, USD, GBP and CAD (look up conversion rates)
            - Charge the conversion fee 5 EUR (convert this too is charging for a different currency)
            - Make sure the funds are not lost due to conversion (except the fee)
            - Currency type must be bound to the account
        
    START THE APP WITH THE ACCOUNT OF YOUR CHOOSING (no need to handle cases where an account doesn't exist)

"""


class Bank_Account():
    def __init__(self, account_holder: str, balance: int) -> None:
        self.account_holder = account_holder
        self.balance = balance
        self.currency = 'EUR'  # default currency when creating a Bank Account


class ATM():
    def __init__(self, joshua) -> None:
        self.accounts = [joshua]  # initial bank account in ATM
        self.current_user = self.accounts[0]  # initial current user

    def menu(self, account):
        print(f"""Menu:
Account: {account.account_holder} ({account.currency})
1. Switch Accounts
2. Create new account
3. Deposit funds
4. Withdraw funds
5. Display current balance
6. Change currency
7. Leave""")

    def deposit(self, account, amount: int):
        account.balance += amount
        print(f"Successfully deposited {amount} {account.currency}.")

    def withdraw(self, account, amount: int):
        if account.balance >= amount:
            account.balance -= amount
            print(f"Successfully withdrawn {amount} {account.currency}.")
        else:
            print(f"Not enough funds to withdraw {amount} {account.currency}.")

    def get_balance(self, account):
        print(f"{account.account_holder} has {
              account.balance} {account.currency}.")

    def switch_account(self):
        for i, acc in enumerate(self.accounts, 1):
            print(f"{i}: {acc.account_holder}")

        while True:
            try:
                name = int(input(
                    "Choose an account by entering the number of the holder you want to switch to: "))
                if name > len(self.accounts):
                    print("Invalid input. No such account with that number.")
                    return
                break  # Exit the loop if successful conversion to int
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.current_user = self.accounts[name - 1]

    def create_account(self, account):
        self.accounts.append(account)
        print(f"{account.account_holder}'s account successfully added.")

    def change_currency(self, account, currency: str):

        rates = {'EUR/GBP': 1.2,
                 'EUR/USD': 0.95,
                 'EUR/CAD': 0.68,
                 'GBP/USD': 0.79,
                 'GBP/CAD': 0.56,
                 'USD/CAD': 0.71
                 }

        if account.currency == currency:
            print("Account is already set to this currency.")
            return

        elif f"{account.currency}/{currency}" in rates.keys():
            account.balance /= rates[f"{account.currency}/{currency}"]

        else:
            account.balance *= rates[f"{currency}/{account.currency}"]
            print(account.balance)

        account.currency = currency
        fee = (5 / rates[f"EUR/{currency}"])  # 5€ fee
        account.balance -= fee


# START initial Bank Account in ATM
joshua = Bank_Account('Joshua Bell', 100)
atm = ATM(joshua)
# END initial Bank Account in ATM

loop = True
while loop:
    atm.menu(atm.current_user)

    command = int(input())

    if command == 1:
        atm.switch_account()

    elif command == 2:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        full_name = first_name + ' ' + last_name
        atm.create_account(Bank_Account(account_holder=full_name, balance=0))

    elif command == 3:
        while True:
            try:
                amount = int(input("Enter amount you want to deposit: "))
                break  # Exit the loop if successful conversion to int
            except ValueError:
                print("Invalid input. Please enter a number.")

        atm.deposit(atm.current_user, amount)

    elif command == 4:
        amount = 0
        withdraw_numbers = [10, 20, 30, 50, 100, 150, 200, 300, 500]
        while True:
            try:
                amount = int(input(
                    "Enter amount you want to withdraw (10, 20, 30, 50, 100, 150, 200, 300, 500): "))
                if amount in withdraw_numbers:
                    break  # Exit the loop if successful conversion to int
                else:
                    print("Invalid amount.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        atm.withdraw(atm.current_user, amount)

    elif command == 5:
        atm.get_balance(atm.current_user)

    elif command == 6:
        available_currencies = ['EUR', 'GBP', 'USD', 'CAD']
        currency = ''
        while True:
            currency = input(
                "Enter the currency you want to change to (EUR, USD, GBP and CAD): ")
            if currency not in available_currencies:
                print("No such currency available.")
            else:
                break
        atm.change_currency(atm.current_user, currency)

    elif command == 7:
        loop = False  # exits App

    else:
        print("Invalid command.")


# OBSERVATIONS
"""
USER REVIEW:
    Switch Accounts:
        - I accidentaly typed 3 instead of 2 when choosing accounts, it took me to the menu and I had to do it all over again...
    
    Deposit funds:
        - Poor self awarenes protocol, I accidentally typed one extra 0 and it didnt ask me to verify the input...
        - Again with the menu...
    
    Withdraw funds:
        - Why is 45 invalid number? If I can type what I want, why am I not allowed to input 99% of numbers??

    Display current balance:
        - I dont want the answer in third person.
        - I dont want to see 1000 decimals behind my number.
        - The damn menu pops right after showing me the balance, I dont wanna have to scroll up to find it.
    
    Change currency:
        - I wanted to change USD to EUR and the app broke...
        - I think Im losing my money when Im changing currencies... This is theft! I might take this to court if proven right.
    
    Other:
        - The first option in the menu is capitalized, others are not, not very professional
        - The app is trash, I wouldn't recommend it to anyone
"""
