from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass


class CreditCard(PaymentMethod):
    def make_payment(self, amount):
        print(f"₹{amount} paid successfully using Credit Card.")


class DebitCard(PaymentMethod):
    def make_payment(self, amount):
        print(f"₹{amount} paid successfully using Debit Card.")


class UPI(PaymentMethod):
    def make_payment(self, amount):
        print(f"₹{amount} paid successfully using UPI.")


class NetBanking(PaymentMethod):
    def make_payment(self, amount):
        print(f"₹{amount} paid successfully using Net Banking.")


class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.make_payment(amount)


# Main Program
amount = float(input("Enter the payment amount: "))

print("\nChoose Payment Method:")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Net Banking")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    payment = CreditCard()
elif choice == 2:
    payment = DebitCard()
elif choice == 3:
    payment = UPI()
elif choice == 4:
    payment = NetBanking()
else:
    print("Invalid choice!")
    exit()

processor = PaymentProcessor(payment)
processor.process_payment(amount) 