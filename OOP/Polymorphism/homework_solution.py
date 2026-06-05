class Payment:
    def __init__(self, name):
        self.name = name

    def pay(self, amount):
        return f"{self.name} pays ${amount}"


class CreditCard(Payment):
    def __init__(self, name, card_number):
        super().__init__(name)
        self.card_number = card_number

    def pay(self, amount):
        return f"{self.name} paid ${amount} using credit card ****{self.card_number[-4:]}"


class PayPal(Payment):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

    def pay(self, amount):
        return f"{self.name} paid ${amount} using PayPal ({self.email})"


payment_methods = [
    CreditCard("Ahmed", "1234567890123456"),
    PayPal("Sara", "sara@email.com")
]

for p in payment_methods:
    print(p.pay(100))
