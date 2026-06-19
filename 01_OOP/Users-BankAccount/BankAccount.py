class BankAccount:
    def __init__(self,interest_rate = 1, balance = 0):
        self.balance = balance
        self.interest_rate = float(interest_rate)

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
        
    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            print(self.balance)

        elif(self.balance < amount):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            print(self.balance)
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        while (self.balance > 0):
            self.balance * self.interest_rate
        return self
        

account1 = BankAccount(0.03, 200)
account1.deposit(200).deposit(300).deposit(400).withdraw(900).yield_interest().display_account_info()

account2 = BankAccount(2, 300)
account2.deposit(200).deposit(300).withdraw(50).withdraw(300).withdraw(10).withdraw(40).yield_interest()

account1.display_account_info()
account2.display_account_info()



