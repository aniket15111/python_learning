class BankAccount:
    def __init__(self,account_holder_name,balance=0):
        self.account_holder_name=account_holder_name
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited amount. New balance is {self.balance}")
    def withdraw(self,withdraw_amount):
        if self.balance<withdraw_amount:
            print(f"insufficient balance : {self.balance}")
        else:
            self.balance-=withdraw_amount
            print(f"{withdraw_amount} withdrawed. New balance {self.balance}")
    def display_balance(self):
        print(f"{self.balance} is the current balance")

account1=BankAccount("Aniket")
account1.deposite(100)
account1.deposite(100)
account1.withdraw(50)
account1.withdraw(200)
account1.display_balance()