class Apartment:
    def show(self):
        return 'Show Apartment:\n'


class OneRoomApartment(Apartment):
    def show(self):
        return 'Show one-room apartment'


class TwoRoomApartment(Apartment):
    def show(self):
        return 'Show two-room apartment'


class Factory:
    def show_choice(self, apart):
        if apart == 'one':
            return OneRoomApartment()
        else:
            return TwoRoomApartment()


f = Factory()
print(f.show_choice('one').show())
print()
print(f.show_choice('two').show())