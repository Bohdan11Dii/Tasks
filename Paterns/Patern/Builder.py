from abc import abstractmethod


class Auto:
    def __init__(self):
        self.data = ''

    def about_auto(self):
        return self.data

    def append_auto(self, s):
        self.data += s


class AutoRealization:
    @abstractmethod
    def name_auto(self): pass

    @abstractmethod
    def auto_machine(self): pass

    @abstractmethod
    def auto_character(self): pass

    @abstractmethod
    def auto_parts(self): pass

    @abstractmethod
    def topping(self): pass

    @abstractmethod
    def info(self): pass


class DiselCar(AutoRealization):
    def __init__(self):
        self.__auto = Auto()

    def name_auto(self):
        self.__auto.append_auto('Volkswagen\n')

    def auto_machine(self):
        self.__auto.append_auto("Disel car\n")

    def auto_character(self):
        self.__auto.append_auto("Engime: 1.9; Body type: sedan\n")

    def auto_parts(self):
        self.__auto.append_auto(
            "Number_of_doors: 4; Icon: W; Color: gray\n")

    def topping(self):
        self.__auto.append_auto("Model: Passat B5; Country: Germany; Price: $5 000  ")

    def info(self):
        return self.__auto


class ElectroCar(AutoRealization):
    def __init__(self):
        self.__auto = Auto()

    def name_auto(self):
        self.__auto.append_auto('Tesla\n')

    def auto_machine(self):
        self.__auto.append_auto('Electro car\n')

    def auto_character(self):
        self.__auto.append_auto(
             "Engime: Three electric motors (one in front, two in the back);"
             "Body type: sedan\n")

    def auto_parts(self):
        self.__auto.append_auto(
            "Number_of_doors: 2;"
            "Icon: T;"
            "Color: black\n"
        )

    def topping(self):
        self.__auto.append_auto(
            "Model: Tesla Roadster;"
            "Country: American;"
            "Price: $20 000 "
        )

    def info(self):
        return self.__auto


class Director:
    def __init__(self, developer):
        self.__developer = developer

    def set_developer(self, developer):
        self.__developer = developer

    def get_info_auto(self):
        self.__developer.name_auto()
        self.__developer.auto_machine()
        self.__developer.auto_character()
        self.__developer.auto_parts()
        self.__developer.topping()
        return self.__developer.info()


if __name__ == '__main__':

    disel_car = DiselCar()
    director = Director(disel_car)

    volkswagen = director.get_info_auto()
    print(volkswagen.about_auto())

    print('-----------------------------------------')

    electro_car = ElectroCar()
    director = Director(electro_car)

    tesla = director.get_info_auto()
    print(tesla.about_auto())
