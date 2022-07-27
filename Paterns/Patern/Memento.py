class Memento:
    def __init__(self, state):
        self.__state = state

    def get_state(self):
        return self.__state[:]


class Registration:
    def __init__(self):
        self.__state = ['Registration page']

    def add_info(self, information):
        print(f'На реєстрації ви заповнили: {information}')
        self.__state.append(information)

    def create_memento(self):
        return Memento(self.__state[:])

    def set_memento(self, memento: Memento):
        self.__state = memento.get_state()

    def __str__(self):
        return f'Зареєстровані дані {self.__state}'


class Client:
    def __init__(self, registr):
        self.register = registr
        self.register_state = []

    def add_info_to_registration(self, information):
        self.register_state.append(self.register.create_memento())
        self.register.add_info(information)

    def get_back(self):
        if len(self.register_state) == 1:
            self.register.set_memento(self.register_state[0])
            print('Ви повернулись на початкову сторінку реєстрації')
            print(self.register)

        else:
            print('Відміна попередньої дії')
            state = self.register_state.pop()
            self.register.set_memento(state)
            print(self.register)


if __name__ == "__main__":
    registr = Registration()
    client = Client(registr)
    print(registr)
    print('-' * 5 + "Заповняєм порожні поля" + 5 * '-')
    client.add_info_to_registration('Bohdan')
    client.add_info_to_registration('Brovdiy')
    client.add_info_to_registration('bodyabrovdiy@gmail.com')
    client.add_info_to_registration('12345678')
    print(registr)
    print('-' * 5 + "Повернтаємось назад" + 5 * '-')
    client.get_back()
    client.get_back()
    client.get_back()
    print('-' * 5 + "Змінюємо внесені зміни" + 5 * '-')
    client.add_info_to_registration('bodyabrovdiy@gmail.com')
    client.add_info_to_registration('jasfjblua4bvb;o8h8')
    print(registr)
