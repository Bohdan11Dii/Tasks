from abc import ABC, abstractmethod
from random import choice
from enum import Enum


class OrderType(Enum):
    SALYAMI = 1
    MARGARITA = 2
    CAPRICHOZA = 3


class Order:
    order_id = 1

    def __init__(self, order_type):
        self.id = Order.order_id
        self.type = order_type
        Order.order_id += 1

    def __str__(self):
        return f"заказ під номером #{self.id} ({self.type.name})"


class Observer:
    @abstractmethod
    def update(self, order_id):
        pass


class Subject(ABC):
    def __init__(self):
        self.observers = []

    def add_client(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def delete(self, observer):
        self.observers.remove(observer)

    def notify(self, order_id):
        for observer in self.observers:
            observer.update(order_id)


class ChiefCook(Subject):
    def __init__(self):
        super().__init__()
        self.orders = []
        self.finish_order = []

    def take_order(self, order):
        print(f'Шеф прийняв {order}')
        self.orders.append(order)

    def get_order(self, order_id):
        order = None
        for it in self.finish_order:
            if it.id == order_id:
                order = it
                break
        self.finish_order.remove(order)
        return order

    def proccesing_order(self):
        if self.orders:
            order = choice(self.orders)
            self.orders.remove(order)
            self.finish_order.append(order)
            print(f'Шеф виконав {order}')
            self.notify(order.id)
        else:
            print('Шeф виконав усі замовлення')


class Client(Observer):
    def __init__(self, name, chief):
        self.chief = chief
        self.name = name
        self.order = None

    def update(self, order_id):
        if self.order is not None:
            if order_id == self.order.id:
                print(f'Клієнт {self.name} забрав '
                      f'{self.chief.get_order(order_id)}')
                self.chief.delete(self)

    def create_order(self):
        order_type = choice([OrderType.SALYAMI,
                             OrderType.MARGARITA,
                             OrderType.CAPRICHOZA])

        self.order = Order(order_type)
        print(f'Клієнт {self.name} зробив {self.order}')
        self.chief.add_client(self)
        self.chief.take_order(self.order)


if __name__ == "__main__":
    names = ['Роман', 'Іван', 'Андрій', 'Настя', 'Діана']

    chief = ChiefCook()
    clients = [Client(name, chief) for name in names]
    for client in clients:
        print("*" * 50)
        client.create_order()
    print("*" * 5 + "Повар приступив до виконання замовлень" + "*" * 5 )
    for i in range(6):
        print("*" * 50)
        chief.proccesing_order()