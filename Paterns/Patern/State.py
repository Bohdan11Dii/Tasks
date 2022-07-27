class Transmission:
    _state = None

    def __init__(self, state):
        self.set_transmission(state)

    def set_transmission(self, state):
        self._state = state
        self._state.transmission = self

    def first_transmission(self):
        self._state.first_transmission()

    def second_transmission(self):
        self._state.second_transmission()


class State:
    def transmission(self):
        self.transmission = Transmission()

    def first_transmission(self):
        pass

    def second_transmission(self):
        pass


class FirstTransmission(State):
    def first_transmission(self):
        print('Already in first transmission')

    def second_transmission(self):
        print('Gearbox moving to second transmission')
        self.transmission.set_transmission(SecondTransmission())


class SecondTransmission(State):
    def first_transmission(self):
        print('Second transmission')
        self.transmission.set_transmission(FirstTransmission())

    def second_transmission(self):
        print('Already in first transmission')


my = Transmission(FirstTransmission())
my.first_transmission()
my.second_transmission()
