# Encapsulation

# class BadBankAccount:
    # def __init__(self,balance):
        # self.balance = balance

#account = BadBankAccount(0.0)
#account.balance = -1



class BankAccount:
    def __init__(self):
        self._balance = 0.0 
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be more than zero!")
        self._balance += amount
    
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be more than zero!")
        if amount >= self._balance:
            raise ValueError(f"Amount can't be greater than balance : {self.balance}")
        self._balance -= amount


account = BankAccount()
print(account.balance)

account.deposit(10)
print(f"old amount {account.balance}")
account.withdraw(1)
print(f"new amount {account.balance}")
account.withdraw(100)

