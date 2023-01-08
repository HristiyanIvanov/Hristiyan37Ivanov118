class Cart:
    def __init__(self, producer, code, unit_price, amount, full_price):
        self.producer = producer
        self.code = code
        self.unit_price = unit_price
        self.amount = amount
        self.full_price = full_price

    def __repr__(self):
        return f'{self.producer} {self.code} {self.unit_price} {self.amount} {self.full_price}'


article = ["Xiaomi Mi Router 4C", "Xiaomi Mi Router 4A", "TP-Link Archer C54 AC1200", "TP-Link Archer C80 AC1900"]

print(article)
cart = []
import random

def add_to_cart():
    while True:
        choose = int(input("Choose article or /5 to quit/: "))
        if choose == 1:
            code = random.randint(0, 150)
            unit_price = 78.56
            amount = int(input("Enter quantity: "))
            full_price = unit_price * amount
            cart.append(Cart(article[0], code, unit_price, amount, full_price))
        elif choose == 2:
            code = random.randint(0, 150)
            unit_price = 56.99
            amount = int(input("Enter quantity: "))
            full_price = unit_price * amount
            cart.append(Cart(article[1], code, unit_price, amount, full_price))
        elif choose == 3:
            code = random.randint(0, 150)
            unit_price = 136.20
            amount = int(input("Enter quantity: "))
            full_price = unit_price * amount
            cart.append(Cart(article[2], code, unit_price, amount, full_price))
        elif choose == 4:
            code = random.randint(0, 150)
            unit_price = 178.36
            amount = int(input("Enter quantity: "))
            full_price = unit_price * amount
            cart.append(Cart(article[3], code, unit_price, amount, full_price))
        elif choose == 5:
            print("End of shopping.")
            print(f"You bought: {cart}")
            break
        else:
            print("Non-existing article!")


def end_price():
    delivery_price = float(input("Delivery Price: "))
    counter = 0
    total_price = dict()
    with open("end_price.txt", "w") as f:
        for router in cart:
            key = counter
            total_price[key] = (1.2 * router.full_price)
            counter += 1
        total = [sum(total_price.values()) + delivery_price]

        f.write(
            f"Delivery price: {delivery_price} BGN | Total: {total} + 20 % VAT")


add_to_cart()
end_price()
