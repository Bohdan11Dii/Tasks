class MakePizza:
    def choice_of_pizz(self):
        pass

    def cook_pizza(self):
        pass

    def eat_pizza(self):
        pass

    def go_to_pizza(self):
        self.choice_of_pizz()
        self.cook_pizza()
        self.eat_pizza()


class PaperoniPizza(MakePizza):
    def choice_of_pizz(self):
        print('Choice of pizza')

    def cook_pizza(self):
        print('Cooking pizza')

    def eat_pizza(self):
        print('Eat pizza')


class SalamiPizza(MakePizza):
    def choice_of_pizz(self):
        print('Choice of pizza')

    def cook_pizza(self):
        print('Cooking pizza')

    def eat_pizza(self):
        print('Eat pizza')


f = PaperoniPizza()
print(f.go_to_pizza())
print()

s = SalamiPizza()
print(s.go_to_pizza())


