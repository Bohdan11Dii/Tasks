class Integer:
    def number_search(self, riddle_number):
        pass


class MoreThan(Integer):
    def number_search(self, riddle_number):
        if riddle_number == "10":
            return 'Ok'


class LessThan(Integer):
    def number_search(self, riddle_number):
        if riddle_number == '20':
            return 'Great'


class IsEqualTo(Integer):
    def number_search(self, riddle_number):
        if riddle_number == '15':
            return 'Finish'


class Determination:
    def __init__(self):
        self.item = []

    def add_item(self, i):
        self.item.append(i)

    def determination(self, riddle_number):
        for i in self.item:
            it = i.number_search(riddle_number)
            if it:
                print('It is ', it)
                break

        else:
            print("You didn't guess the number")

det = Determination()
det.add_item(MoreThan())
det.add_item(LessThan())
det.add_item(IsEqualTo())
det.determination("10")
# det.determination("20")
# det.determination("25")

