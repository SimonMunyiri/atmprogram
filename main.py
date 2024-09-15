# CREATING AN ATM APP

print("A SIMPLE ATM APP")

bankBalance = 0


while True:
    print("Please select an action .")
    print("1) Deposit.")
    print("2) Withdraw.")
    print("3) Lipa na Bank.")
    check = input("> ")
    if check == "1":
        print("Attempting to deposit.")
        #ask the user the amount that he/she wants to deposit
        print("Enter amount of money to deposit.")
        moneyDepositAmount = int(input("> "))

        #add the deposited amount to the bank balance
        bankBalance += moneyDepositAmount

        #print the new bank balance
        print(f"The new bank balance is {bankBalance}.")
    elif check == "2":
        print("Withdrawing")
        #allow the user to enter the amount of money he/she wants to withdraw
        withdrawalAmount = int(input("> Ksh "))

        #check if the bank account balance is more than the amount
        #that the user wants to withdraw
        if withdrawalAmount <= bankBalance:
            #proceed to withdraw
            bankBalance -= withdrawalAmount #this the new amount after the user has withdrawn

            #print the new bank balance and the amount withdrawn
            print(f"You have withdrawn {withdrawalAmount}. Your new bank balance is {bankBalance}")
        else:
            #user can't withdraw
            #print an error
            print(f"Sorry, you can't withdraw ksh {withdrawalAmount}. Your bank balance is {bankBalance}")
    elif check == "3":
        #proceed to lipa na bank option

        #enter the paybill number
        payBill = int(input("Paybill: >"))

        #amount to pay
        amount = int(input("Amount: >"))

        #check if the bank balance is enough to pay the specified amount
        if bankBalance < amount:
            print(f"You have insufficient money to send {amount} to {payBill}.")
        else:
            #make the payments
            #deduct the amount payed from the bank account balance
            bankBalance -= amount
            #print the new bank balance and a success message
            print(f"You have successfully sent {amount} to {payBill}. Your new bank account balance is {bankBalance}")




