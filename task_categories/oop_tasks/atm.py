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

import time

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
        print(f"""--------------------------
Menu:
Account: {account.account_holder} ({account.currency})
1. Switch accounts
2. Create new account
3. Deposit funds
4. Withdraw funds
5. Display current balance
6. Change currency
7. Leave""")

    def deposit(self, account, amount: int):
        account.balance += amount
        print(f"Successfully deposited {amount} {account.currency}.")

    def withdraw(self, account, idx: int):
        withdraw_numbers = [10, 20, 30, 50, 100, 150, 200, 300, 500]
        amount = withdraw_numbers[idx - 1]
        if account.balance >= amount:
            account.balance -= amount
            print(f"Successfully withdrawn {amount} {account.currency}.")
        else:
            print(f"Not enough funds to withdraw {amount} {account.currency}.")
            print("Check your balance to see how much money you can withdraw.")
            time.sleep(3) # extra time to read

    def get_balance(self, account):
        # Why was this differently formated? Your change gave me an error (SyntaxError: unterminated string literal (detected at line 82))
        # Linter did it. If the line is too long, you need to break it but you need to add \ at the end for the code not to break (no idea why linter doesn't)
        print(f"Your account balance: {account.balance:.2f} {account.currency}.")  # Here is an example

    def switch_account(self):
        for i, acc in enumerate(self.accounts, 1):
            print(f"{i}: {acc.account_holder}")

        while True:
            try:
                name = int(input(
                    "Choose an account by entering the number of the holder you want to switch to: "))
                if name > len(self.accounts) or name < 1:
                    print("Invalid input. No such account with that number.")
                    return False
                break  # Exit the loop if successful conversion to int
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.current_user = self.accounts[name - 1]
        return True

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

        account.currency = currency
        if currency == 'EUR':
            fee = 5
        else:
            fee = (5 / rates[f"EUR/{currency}"])  # 5€ fee

        if account.balance >= fee:
            account.balance -= fee
        else:
            print("You don't have sufficient funds to change currency.")
            print("Minimum required: 5 EUR (currency change fee).2")

# START initial Bank Account in ATM
joshua = Bank_Account('Joshua Bell', 100)
atm = ATM(joshua)
# END initial Bank Account in ATM

print("Loading menu...")

loop = True
while loop:
    time.sleep(3) # default seconds of time to read, before the menu appears 
    atm.menu(atm.current_user)

    command = int(input())

    if command == 1:
        while not atm.switch_account():
            continue

    elif command == 2:
        first_name = input(
            "Enter first name: ")
        last_name = input(
            "Enter last name: ")
        full_name = first_name + ' ' + last_name
        atm.create_account(Bank_Account(account_holder=full_name, balance=0))

    elif command == 3:
        while True:
            try:
                amount = int(input(
                    "Enter amount you want to deposit: "))
                confirm = input(
                    "Are you sure you want to deposit this amount (type 'y' for 'yes', any other input is 'no')? ")
                if confirm == 'y':
                    break  # Exit the loop if successful conversion to int
                else:
                    continue

            except ValueError:
                print("Invalid input. Please enter a number.")

        atm.deposit(atm.current_user, amount)

    elif command == 4:
        # available_funds = atm.current_user.balance  # available funds of current user
        withdraw_numbers = [10, 20, 30, 50, 100, 150, 200, 300, 500]
        # if available_funds >= withdraw_numbers[0]:
        #     print("This is the list of options you can withdraw:")
        #     len_ = 0
        for i, num in enumerate(withdraw_numbers, 1):
            print(f"{i}: {num}")

        while True:
            try:
                idx = int(input(
                    f"Enter the number in front of the amount you want to withdraw (1 - 9): "))
                if idx >= 1 and idx <= 9:
                    break  # Exit the loop if successful conversion to int
                else:
                    print("Invalid amount.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")

        atm.withdraw(atm.current_user, idx)



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
        confirm = input("""Changing currency will cost the equivalent of 5 EUR to whatever currency you are changing to.
Do you still want to proceed (type 'y' for 'yes', any other input is 'no')? """) 

        if confirm == 'y':
            atm.change_currency(atm.current_user, currency)
            print(f"Successfully changed currency to {currency}.")

    elif command == 7:
        loop = False  # exits App
        print("Exiting app...")

    else:
        print("Invalid command.")


# OBSERVATIONS
"""
USER REVIEW:
    Switch Accounts:
        - I accidentaly typed 3 instead of 2 when choosing accounts, it took me to the menu and I had to do it all over again...
    
    Fix: 
        - The ATM keeps asking the user to pick the number of an account until the user enters a bank account number that exists in the ATM, so it
        doesn't go straight to the menu when an invalid account number is picked.
        - After every failed attempt, the ATM displays the possible bank account numbers to choose from
            - Q: Should the list of bank accounts only be displayed once, or even after every failed attempt?
            - A: The complaint here was about going to the menu after choosing an invalid selection.
            You fixed it well, only thing thats missing is the 0 in the menu, telling the user they can type 0 to go back since you added that logic.
                - Only existing accounts can be chosen
    
    Deposit funds:
        - Poor self awarenes protocol, I accidentally typed one extra 0 and it didnt ask me to verify the input...
        - Again with the menu...
    
    Fix:
        - The ATM now asks if the user to confirm the amount they want to deposit
        - U: You can make it more user friendly, the key is to make it as simple as possible but as informative as possible
        - The menu has now a user-friendlier format, showing when it starts
            - Q: How else can the menu be displayed? It has to automatically display for the next command
            - A: There is a time.sleep() method that waits for a number of seconds before continuing with the rest of the execution, allowing smoother console interactions.
                - Implemented for every appearance of the menu
    Withdraw funds:
        - Why is 45 invalid number? If I can type what I want, why am I not allowed to input 99% of numbers??
    
    Fix:
        - 45 was an invalid number as the only numbers the ATM accepts are 10, 20, 30, 50, 100, 150, 200, 300 and 500
        - This has been fixed so that the user has to enter the number in front of the possible withdraw amounts (see function withdraw())
        - Now the ATM only gives the list of options the user can actually withdraw as it checks their balance beforehand
            - Q: Shoould the ATM always list all options (10, 20, 30, 50, 100, 150, 200, 300 and 500) and then only after the user chooses an amount, say if 
            it is possible to withdraw that amount? 
                - This is why I left some lines commented in the function, in case of a different implementation
            - A: Yes, the fix was to make it appear in the same style as the menu, choosing numbers.
                - Done!

    Display current balance:
        - I dont want the answer in third person.
        - I dont want to see 1000 decimals behind my number.
        - The damn menu pops right after showing me the balance, I dont wanna have to scroll up to find it.

    Fix:
        - It's in second person
        - U: Better way is to display it as: "Your account balance: 100 EUR"
            - Done
        - It shows only 2 decimal points (just like real money)
        - It's easier to find the print statements before the menu
        - U: Again, it appears right away, if there are users with only 2 lines of console available, its an awful UX
    
    Change currency:
        - I wanted to change USD to EUR and the app broke...
        - I think Im losing my money when Im changing currencies... This is theft! I might take this to court if proven right.
    
    Fix:
        - Changing currency to EUR is now possible
        - Losing money is actually part of changing currencies. This can be checked by returning back to EUR and seeing if the amount has been deducted 5 EUR
        for every change of currency
        - U: Fix was to let the user know before changing that it costs 5 EUR equivalent in the currency their account is using.
        Users need to be informed about everything, especially about stuff that directly affects them.
            - User is now informed about the fee.
            - The ATM checks if the user has sufficient funds to change currency

    Other:
        - The first option in the menu is capitalized, others are not, not very professional
        - The app is trash, I wouldn't recommend it to anyone

    Fix:
        - Only first word is capitalized
        - It ain't trash anymore ;)
        - U: Little better, still bad UX
            - Any suggestions?

        
    The key takeaway from this user review mock is to always test your app like a user that knows what the app can do but wants it made in the simplest way possible.
    You have to doubt yourself here and test your app with a mindset that there are 100s of better apps that do the same thing as yours. Then you bust your ass to improve it, and repeat the cycle.

    I will take a look at the code after the user is satisfied.
"""
