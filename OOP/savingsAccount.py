class SavingsAccount:
    #Constructor with 2 Attributes with 0 as default for balance
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    #Add amount to balance and display balance
    def makeDeposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount:.2f} accepted.")
        self.displayBalance()

    #Subtract amount from balance and display balance. print insufficient funds if amount is greater than balance
    def makeWithdrawal(self, amount):
        if self.balance < amount:
            print("Insufficient funds, transaction denied.")
        elif amount == 0 :
            print("Invalid amount, transaction denied.")
        else :
            self.balance -= amount
            print(f"Withdrawal of ${amount:.2f} accepted.")
            self.displayBalance()
    #Display Balance of account round to 2 numbers after decimal
    def displayBalance(self):
        print(f"Balance: ${self.balance:.2f}")