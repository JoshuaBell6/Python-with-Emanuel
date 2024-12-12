## ATM review

- ### Switch accounts

  - After choosing this option user needs to be presented with a short description before listing accounts
  - Input text should be as concise as possible ("Enter a number" is more than enough) everything else should be described on top.
  - The menu doesn't have a back option
  - The menu doesn't indicate which account is currently selected
  - User is left waiting for no reason before getting the menu back (using sleep isn't the solution everywhere)

- ### Create new account

  - After you enter the account, you just go back to the menu (again, waiting for too long) forcing the user to select switch account afterwards
  - Best way would be to ask a user if they want to use the account or just select it automatically (first option is the best)

- ### Deposit funds

  - Any other option is 'no' is not good because users can accidentaly type something other than 'y' and then they have to redo the process ('y', 'n' is actually the standard)
  - Good UX is to give the user info which currency they are depositing in

- ### Withdraw funds

  - Again, input should be as concise as possible
  - Another good UX is to display which currency the user is withdrawing the funds in
  - Back option is also needed here

- ### Change curreny
  - Changing from EUR to GBP took me from 45 EUR to 33.33 GBP (somethin' aint right)
  - Inform the user about the fee before choosing to change the currency and ask if they want to proceed
  - Good UX is to calculate the fee in the current currency and display that information, not "5 EUR of whatever currency"
  - Allow user to type letters in any form when choosing currency (or better yet, make the same menu as everything else)
  - NO BACK OPTION
