from abc import ABC


class Crypto(ABC):
    def show_name(self):
        raise NotImplementedError


class PopularCrypto:
    def __init__(self, name, price):
        self.name= name
        self.price = price

    def __str__(self):
        return (f'{self.name}, my price - {self.price} $')


class UsualCrypto:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return(f'{self.name}, my price - {self.price} $')


class OneProduct:
    def show_name(self):
        return PopularCrypto('Bitcoin',  20000)


class SecondProduct:
    def show_name(self):
        return UsualCrypto('Dogecoin',  0.08)


def get_product(product):
    if product == 1:
        return OneProduct()
    if product == 2:
        return SecondProduct()


def menu():
    while True:
        name_crypto = input("""
        1  - Bitcoin
        2 - Kusama
        """)

        if name_crypto == '1':
            product = get_product(1)
            print(product.show_name())

        if name_crypto == '2':
            product = get_product(2)
            print(product.show_name())
            break

menu()
