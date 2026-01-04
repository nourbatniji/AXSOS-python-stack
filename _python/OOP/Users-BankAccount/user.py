from BankAccount import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def deposit(self, amount):
        self.account.balance += amount
        print(self.account.balance)
        return self

    def withdraw(self, amount):
        self.account.balance -= amount
        print(self.account.balance)
        return self
    
    def display_account_info(self) :
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self

    def transfer_money(self, otheruser, amount):
        self.account.balance -= amount
        otheruser.account.balance += amount
        print(f"Transferred {amount} from {self.name} to {otheruser.name}")
        self.display_account_info()
        otheruser.display_account_info()
        return self

user1 = User("Ahmed")
user1.account.deposit(200).account.deposit(30).account.deposit(500).account.withdraw(300).account.display_account_info()

user2 = User("Mohammed") 
user2.deposit(350).deposit(100).withdraw(50).withdraw(30).display_account_info()

user3 = User("Ali") 
user3.deposit(850).withdraw(50).withdraw(30).withdraw(300).display_account_info()

user1.transfer_money(user3, 400)