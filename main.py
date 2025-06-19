from SavingsAccount import SavingsAccount
from CheckingsAccount import CheckingAccount

savings1 = SavingsAccount("Brendon Kaas", 2000, 50, "10234", "987654", 0.05)
savings1.apply_interest()
savings1.print_customer_information()

print("\n")

savings2 = SavingsAccount("Akash Simmons", 1500, 50, "4000", "987654", 0.04)
savings2.apply_interest()
savings2.print_customer_information()

print("\n")

checking1 = CheckingAccount("Professor Mohsen", 5000, 100, "3500", "987654", 1000)
checking1.transfer(500, savings2)
checking1.print_customer_information()
print()
savings2.print_customer_information()

print("\n")

checking2 = CheckingAccount("Brendon Kaas", 1000, 50, "", "987654", 300)
checking2.transfer(500, savings1)
checking2.print_customer_information()