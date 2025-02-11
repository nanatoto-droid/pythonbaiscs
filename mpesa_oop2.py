from abc import ABC, abstractmethod


# Encapsulation
class Account:
    def __init__(self, account_id, holder_name, balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):  # Corrected spelling
        print(f"Attempting to withdraw {amount} from account with balance {self.balance}")
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount} from account. New balance: {self.balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

    def get_holder(self):
        return self.holder_name


class Customer(Account):
    def __init__(self, account_id, holder_name, balance, phone_number):
        super().__init__(account_id, holder_name, balance)
        self.phone_number = phone_number


# Polymorphism
class Transaction:
    def __init__(self, amount):
        self.amount = amount

    def execute(self, account):
        pass


class DepositTransaction(Transaction):
    def execute(self, account):
        account.deposit(self.amount)


class WithdrawTransaction(Transaction):
    def execute(self, account):
        account.withdraw(self.amount)  # Corrected spelling


# Abstraction
class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class MpesaPaymentSystem(PaymentSystem):
    def process_payment(self, amount):
        print(f"Processing Mpesa payment of {amount}")


# Example usage
mpesa = MpesaPaymentSystem()
account = Customer(1, "Imani", 2000, 712345678)
deposit = DepositTransaction(450)
withdraw = WithdrawTransaction(1780)

deposit.execute(account)  # Fixed variable name
withdraw.execute(account)  # Fixed variable name

print(f"The balance of {account.get_holder()} is {account.get_balance()}")
