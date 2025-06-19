from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, recipient):
        if amount > self.transfer_limit:
            print(f"Transfer Rejected: Transfer Greater Than Limit (${self.transfer_limit})")
        elif self.current_balance - amount < self.minimum_balance:
            print("Transfer Rejected: Insufficient Funds")
        else:
            self.current_balance -= amount
            recipient.deposit(amount)
            print(f"Valid Transfer: ${amount} Sent To {recipient.customer_name}")