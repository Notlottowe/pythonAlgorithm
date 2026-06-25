# Static Vs. Instance Method Examples


class BankAccount:

    MIN_BALANCE = 100
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self,amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("depoit",amount)
        else:
            print("depoit amount must be positive")
    
    def _is_valid_amount(self,amount): # protected method
        return amount > 0

    def __log_transaction(self,transaction_type,amount): # private method
        print(f"Loggin {transaction_type} of ${amount}. New balance: ${self._balance}")

    @staticmethod
    def is_value_interest_rate(rate):
        return 0 <= rate <= 5

account = BankAccount("Alice", 500)
account.deposit(100)



print(BankAccount.is_value_interest_rate(3))
print(BankAccount.is_value_interest_rate(10))