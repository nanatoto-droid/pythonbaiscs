from abc import ABC ,abstractmethod
from mimetypes import inited


# encapsulation
class Account :
    def __init__(self,account_id,holder_name,balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance =balance

    def deposit(self,amount):
        self.balance +=amount
        print(f"deposited{amount}.New balance:{self.balance}")

    def widraw(self,amount):
        print(f"attempting to withraw {amount}from account with balance{self.balance} ")
        if amount <= self.balance:
            self.balance -=amount
            print(f"withraw{amount} from account with balance {self.balance}")

        else:
            print("insuffient balance")

    def get_balance(self):
        return self.balance
    def get_holder(self):
        return self.holder_name


class Customer(Account):
    def __init__(self,account_id,holder_name,balance,phone_number ):
        super().__init__(account_id,holder_name,balance)
        self.phone_number=phone_number

        # polymorphism
class Transaction:
    def __init__(self,amount):
        self.amount=amount

    def execute(self,account):
        pass

class DepositTransaction(Transaction):
    def execute(self, account):
        account.deposit(self.amount)


class WithdrawTransaction(Transaction):
    def execute(self,account):
        account.widraw(self.amount)


 #Abstraction
 class PaymentSystem(ABC):
     @abstractmethod
     def process_payment(self,amount):
         pass

class  MpesaPaymentSystem(PaymentSystem):
    def process_payment(self,amount):
        print(f"processing Mpesa payment of{amount}")

 # example usage
mpesa=MpesaPaymentSystem()
account=Customer(1,"Imani",2000,712345678)
deposit=DepositTransaction(450)
Withdraw=WithdrawTransaction(1780)

deposit.execute(account1)
withdraw.execute(account2)
print(f"the balance of {1.get_holder_name()}is {1.get_balance}")











