from abc import abstractmethod


class Technology:
    """  Реалізація абстрактного класу для технології"""
    def get_model(self, name):
        self.name = name._name


    @abstractmethod
    def find_inches(self):
        pass


class Laptops(Technology):
    def __init__(self, centimeters, name):
        self.centimeters = centimeters
        super().get_model(name)

    def find_inches(self):
        return self.centimeters / 2.54

    def __str__(self):
        return f'I am a laptop, my name is {self.name} and I have {int(self.find_inches())} inches'


class Television(Technology):
    def __init__(self, centimeters, name):
        self.centimeters = centimeters
        super().get_model(name)

    def find_inches(self):
        return self.centimeters * 2.54

    def __str__(self):
        return f'I am a television, my name is {self.name} and I have {int(self.find_inches())} inches'


class Name:
    """ Інтерфейс для реалізації """
    def model_name(self):
        pass


class Asus(Name):
    def __init__(self):
        self.model_name()

    def model_name(self):
        self._name = 'Asus'


class Samsung(Name):
    def __init__(self):
        self.model_name()

    def model_name(self):
        self._name = 'Samsung'


l = Laptops(56, Asus())
print(l)


t = Television(254, Samsung())
print(t)
