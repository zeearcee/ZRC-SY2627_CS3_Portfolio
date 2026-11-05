# Polymorphism with Abstract Classes (Intermediate)
# Scenario: Different payment methods must implement their own payment process.

# Python's abc module allows us to define abstract classes and methods.

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class GCash(Payment):
    def process_payment(self, amount):
        val = .10
        print(f"Paid ₱{amount * val} using GCash.")


class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Paid ₱{amount} using Credit Card.")


class BankTransfer(Payment):
    def process_payment(self, amount):
        print(f"Paid ₱{amount} using Bank Transfer.")


# Creating objects
payments = [
    GCash(),
    CreditCard(),
    BankTransfer()
]

# Polymorphism
for payment in payments:
    payment.process_payment(1000)



# Payment is an abstract parent class.
# The abstract method process_payment() establishes a required interface.
# Every child class provides its own implementation.
# You cannot directly instantiate the abstract Payment class.