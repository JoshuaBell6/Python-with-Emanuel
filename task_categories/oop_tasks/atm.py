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
