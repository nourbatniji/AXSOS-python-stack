class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        print(self.balance)
        return self
    
    def display_user_balance(self) :
        print(f"User: {self.name}, Balance: {self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        print(f"Transferred {amount} from {self.name} to {other_user.name}")
        self.display_user_balance()
        other_user.display_user_balance()
        return self

user1 = User("Ahmed")
user1.make_deposit(200).make_deposit(30).make_deposit(500).make_withdrawal(300).display_user_balance()

user2 = User("Mohammed") 
user2.make_deposit(350).make_deposit(100).make_withdrawal(50).make_withdrawal(30).display_user_balance()

user3 = User("Ali") 
user3.make_deposit(850).make_withdrawal(50).make_withdrawal(30).make_withdrawal(300).display_user_balance()

user1.transfer_money(user3, 400)