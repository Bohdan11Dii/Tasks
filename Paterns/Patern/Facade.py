class Client:
    def __init__(self, name):
        self.name = name

    def hello_name(self):
        print('Доброго дня,', self.name)
        return self.name


class Telephone:
    def product(self):
        department = {'1': 'to change actions', '2': 'for forwarding to a free coordinator', '3': 'for exit'}
        help_information = (
            f'Доброго дня, ви зателефонували до оператора, щоб дізнатись певний вид інформації натисніть \n{department}')
        print(help_information)
        choice = input("Your choice?\n")
        if choice in department.keys():
            if choice == '1':
                print("To change the promotion, you need to contact the branch")
            elif choice == '2' == "for forwarding to a free coordinator":
                print('Wait 5 secondes...')
            elif department.values() == 'for exit':
                print('Goodbye, thank you for choosing our network')

        else:
            print("Sorry, but this choice does not exist")


class Facade:
    def __init__(self):
        self.client = Client("Bohdan")
        self.telephone = Telephone()

    def show(self):
        self.client.hello_name()
        self.telephone.product()


f = Facade()
print(f.show())



