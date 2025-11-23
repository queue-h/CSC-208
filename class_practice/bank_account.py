class BankAccount:
    # will overload the method and initialize balance to zero if no balance given
    def __init__(self, id, name, initial_balance = 0):
        self.id = id
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def get_balance(self):
        return self.balance


def main():
    new_account = BankAccount(1, "Penny Lou", 100)
    new_account.deposit(100)
    print(new_account.get_balance())
    new_account.withdraw(50)
    print(new_account.get_balance()) 
main()