from abc import ABC, abstractmethod


class ItemVisitor(ABC):
    """Інтерфейс для відвідувача"""
    @abstractmethod
    def visit(self, item):
        pass


class ItemElement(ABC):
    """Інтерфейс для продуктів"""
    @abstractmethod
    def accept(self, visitor):
        pass


class Pizza(ItemElement):
    """Клас для замовлення піци"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def accept(self, visitor):
        return visitor.visit(self)


class IceDrink(ItemElement):
    """Клас для замовлення золодного напою"""
    def __init__(self, name, price, capacity):
        self.name = name
        self.price = price
        self.capacity = capacity

    def get_price(self):
        return self.price

    def get_capacity(self):
        return self.capacity

    def accept(self, visitor):
        return visitor.visit(self)


class AmountWithoutDiscount(ItemVisitor):
    """Без знижки"""
    def visit(self, item):
        number = 0
        if isinstance(item, Pizza):
            number = item.get_price()
        elif isinstance(item, IceDrink):
            number = item.get_price()
        return number


class PizzaDiscount(ItemVisitor):
    """Знижка на піццу 15%"""
    def visit(self, item):
        number = 0
        if isinstance(item, Pizza):
            number = item.get_price()
            number -= number * 0.15
        elif isinstance(item, IceDrink):
            number = item.get_price()
        return number


class IceDrinkDiscount(ItemVisitor):
    """Знижка на напій 25%"""
    def visit(self, item):
        number = 0
        if isinstance(item, Pizza):
            number = item.get_price()
        elif isinstance(item, IceDrink):
            number = item.get_price()
            number -= number * 0.25
        return number


class PizzaDiscountAndIceDrinkDiscount(ItemVisitor):
    """Знижка на все 20%"""
    def visit(self, item):
        number = 0
        if isinstance(item, Pizza):
            number = item.get_price()
        elif isinstance(item, IceDrink):
            number = item.get_price()
        number -= number * 0.20
        return number


class Waiter:
    def __init__(self, discount):
        self.order = []
        self.discount = discount

    def set_order(self, order):
        self.order = order

    def set_discount(self, discount):
        self.discount = discount

    def calculate(self):
        price = 0
        if self.order:
            for item in self.order:
                price += item.accept(self.discount)
        return price


if __name__ == "__main__":
    order = [Pizza('Салямі', 89),
             IceDrink("Холодний апельсиновий коктель", 42, 0.5),
             Pizza('Маргарита', 60),
             IceDrink("Холодний шоколадний коктель", 38, 0.5)
             ]

    discount = AmountWithoutDiscount()
    waiter = Waiter(discount)
    waiter.set_order(order)
    print(f"Загальна сума без скидок: {waiter.calculate()} грн")

    discount = PizzaDiscount()
    waiter = Waiter(discount)
    waiter.set_order(order)
    print(f'Загальна сума з урахуванням знижки на піццу: {waiter.calculate()} грн')

    discount = IceDrinkDiscount()
    waiter = Waiter(discount)
    waiter.set_order(order)
    print(f'Загальна сума з урахуванням знижки на напій: {waiter.calculate()} грн')

    discount = PizzaDiscountAndIceDrinkDiscount()
    waiter = Waiter(discount)
    waiter.set_order(order)
    print(f'Загальна сума з урахуванням знижки на все: {waiter.calculate()} грн')