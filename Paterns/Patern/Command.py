from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def realizate(self):
        pass


class ChiefCook:
    def processes_orders(self):
        print('Шеф обробляє отримане замовлення')

    def cooking_food(self):
        print('Кухар готує їжу')

    def gives_order_to_waiter(self):
        print('Кухар віддає готове замовлення офіціанту')


class Waiter:
    def takes_orders(self):
        print('Офіціант принимає замовлення від клієнта')

    def gives_order_to_chef(self):
        print('Офіціант віддає замовлення кухарю')

    def receives_an_order(self):
        print('Офіціант отримує готове замовдення від кухара і відносить клієнту')

    def good_appetite(self):
        print('Офіціант віддає замовлення клієнту і бажає гарного апетиту')


class Client:
    def makes_an_order(self):
        print('Клієнт робить замовлення в офіціанта')

    def enjoys_food(self):
        print('Клієнт отримує своє замовлення і насолоджується їжею')


class ProcessesOrders(Command):
    def __init__(self, executor):
        self.executor = executor

    def realizate(self):
        self.executor.processes_orders()


class CookingFood(Command):
    def __init__(self, executor):
        self.executor = executor

    def realizate(self):
        self.executor.cooking_food()


class GivesOrderToWaiter(Command):
    def __init__(self, executor):
        self.executor = executor

    def realizate(self):
        self.executor.gives_order_to_waiter()


class TakesOrders(Command):
    def __init__(self, executor):
        self.executor = executor

    def realizate(self):
        self.executor.takes_orders()


class GivesOrderToChef(Command):
    def __init__(self, executor):
        self.executor = executor

    def realizate(self):
        self.executor.gives_order_to_chef()


class ReceivesAnOrder(Command):
    def __init__(self, executor):
        self.executor = executor

    def realizate(self):
        self.executor.receives_an_order()


class GoodAppetite(Command):
    def __init__(self, executor):
        self.executor = executor

    def realizate(self):
        self.executor.good_appetite()


class MakesAnOrder(Command):
    def __init__(self, executor):
        self.executor = executor

    def realizate(self):
        self.executor.makes_an_order()


class EnjoysFood(Command):
    def __init__(self, executor):
        self.executor = executor

    def realizate(self):
        self.executor.enjoys_food()


class Order:
    def __init__(self):
        self.history = []

    def add_command(self, command):
        self.history.append(command)

    def get_order(self):
        if not self.history:
            print('Не поставлене правильне виконання команд для замовлення')
        else:
            for item in self.history:
                item.realizate()


if __name__ == '__main__':
    chief = ChiefCook()
    waiter = Waiter()
    client = Client()
    order = Order()

    order.add_command(MakesAnOrder(client))
    order.add_command(TakesOrders(waiter))
    order.add_command(GivesOrderToChef(waiter))
    order.add_command(ProcessesOrders(chief))
    order.add_command(CookingFood(chief))
    order.add_command(GivesOrderToWaiter(chief))
    order.add_command(ReceivesAnOrder(waiter))
    order.add_command(GoodAppetite(waiter))
    order.add_command(EnjoysFood(client))

    order.get_order()