class Car:
    def __init__(self, name, model, release_year):
        self.name = name
        self.model = model
        self.release_year = release_year


class CarFlyweight:
    def __init__(self):
        self.cars = []

    def cars_factory(self, name, model, release_year):
        car = []
        for item in self.cars:
            if item.name == name and item.model == model and item.release_year == release_year:
                car.append(item)
        if not car:
            car = Car(name, model, release_year)
            self.cars.append(car)

    def get_car(self):
        print('Cars: ')
        for car in self.cars:
            print(car.name + ' ' + car.model + ' ', car.release_year)


def menu():
    cf = CarFlyweight()
    cf.cars_factory('BMW', 'Sedan', 2013)
    cf.cars_factory('Tesla', 'Sedan', 2020)
    cf.cars_factory('Tesla', 'Sedan', 2020)
    cf.cars_factory('BMW', 'Sedan', 2013)
    cf.cars_factory('Volvo', 'Sedan', 2013)


    cf.get_car()


if __name__ == '__main__':
    menu()