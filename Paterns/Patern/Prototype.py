import copy
from abc import ABC


class AbstractPizza(ABC):
    def __init__(self):
        self.name = None
        self.souce = None
        self.cooking_time = None
        self.topping = None


class SalyamiPizza(AbstractPizza):
    def __init__(self, name, souce, cooking_time):
        super().__init__()

        self.name = name
        self.souce = souce
        self.cooking_time = cooking_time

    def __str__(self):
        info = f"Pizza name: {self.name} \n" \
               f"souce :{self.souce} \n" \
               f"cooking_time :{self.cooking_time}\n" \

        return info


if __name__ == '__main__':

    s = SalyamiPizza('Salami', 'Tomato', '10 minute')
    print(s)

    new_pizza = copy.copy(s)
    new_pizza.name = 'Pronto'
    print(new_pizza)

    new_pizza_1 = copy.deepcopy(s)
    new_pizza_1.name = 'Margarita'
    print(new_pizza_1)
