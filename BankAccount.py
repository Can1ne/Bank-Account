# Partner - Brendon Kaas
class BankAccount:
    bank_title = "Bank on Craver Road"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.__account_number = account_number
        self.__routing_number = routing_number
        

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Transaction Declined: Cannot Withdraw More Than Current Balance!")
        else:
            self.current_balance -= amount

    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer: {self.customer_name}")
        print(f"Balance: $${self.current_balance}")
        print(f"Minimum Balance Requirement: $${self.minimum_balance}")
        print(f"Account Number: {self.__account_number}")
        print(f"Routing Number: {self.__routing_number}")



