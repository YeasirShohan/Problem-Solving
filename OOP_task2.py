#OOP
#Task02
"""Create Account class with 2 attributes balance and account no. 
Then create method for debit credit and printing the balance."""

class Account:
    def __init__(self, account, balance):
        self.account_no = account
        self.balance = balance

    #Cradit method    
    def cradit(self, amount):
        self.balance += amount
        if amount>=0:
            print("BDT- ", amount, "added in your account")
            print("Total BDT- ", self.final_balance())
        else:
            print("Invalide")
    
    #debit method
    def debit(self, amount):
        self.balance -= amount
        if amount<1 or amount>self.balance:
            print("Insufficient Balance")
        else:
            print("BDT- ", self.balance, "was left in your account")

    def final_balance(self):
        return self.balance
    

acc1 = Account(1, 00)
acc1.cradit(int(input("Enter the Adding amount- ")))
acc1.debit(int(input("Enter your debited amount- ")))