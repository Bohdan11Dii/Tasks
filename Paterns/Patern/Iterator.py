class Game:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Ви проходите {self.number} рівень гри'


class Iterable:
    def __init__(self, amount_slices):
        self.slices = [Game(i + 1) for i in range(amount_slices)]
        print(f'Розпочніть гру, яка містить {amount_slices} рівнів')

    def __iter__(self):
        return Iterator(self.slices)


class Iterator:
    def __init__(self, game):
        self.game = game
        self.index = 0

    def __next__(self):
        try:
            item = self.game[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration
        return item


if __name__ == "__main__":
    it = Iterable(10)
    for item in it:
        print(item)


