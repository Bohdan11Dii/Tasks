from abc import abstractmethod


class Strategy:
    @abstractmethod
    def section(self):
        pass


class Bus(Strategy):
    def __init__(self, price):
        self.price = price

    def section(self):
        print(f"I have {self.price}, so I will take the Bus")


class Bicycle(Strategy):
    def __init__(self, price):
        self.price = price

    def section(self):
        print("I don't have one, so I'll go by Bicycle")


class Taxi(Strategy):
    def __init__(self, price):
        self.price = price

    def section(self):
        print(f'I have {self.price}, so I will take the Taxi')


class StrategyRun:
    def go_choice(self):
        s1 = input('Make a choice\n'
                   'Bus, Bicycle or Taxi\n')
        if s1 == "Bus":
            return Bus('10$').section()

        elif s1 == "Bicycle":
            return Bicycle(None).section()

        elif s1 == "Taxi":
            return Taxi('30$').section()


s = StrategyRun()
s.go_choice()


