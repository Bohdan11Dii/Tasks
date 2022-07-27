class Transport:
    def move(self, name):
        raise NotImplementedError


class Car(Transport):
    def move(self, name):
        return f"{name} moving along the road"


class Boat(Transport):
    def move(self, name):
        return f'{name} moving on water'


class Composite(Transport):
    def __init__(self):
        self.items = []

    def move(self, name):
        print("Transport :")
        for obj in self.items:
            obj.move()

    def add(self, obj):
        if isinstance(obj, Transport) and not obj in self.items:
            self.items.append(obj)

    def get_item(self, index):
        return self.items[index]


info = Composite()
info.add(Car())
info.add(Boat())


def menu():
    while True:
        help = input('Your choice of transport\n'
                     '1 - car\n'
                     '2 - boat\n'
                     'q - exit\n')

        if help == '1':
            item = info.get_item(0)
            print(item.move('BMW'))

        elif help == '2':
            item = info.get_item(1)
            item.move('Marian')
        elif help == 'q':
            break


menu()