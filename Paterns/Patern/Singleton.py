class Singleton:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, password, email):
        self.user = user
        self.password = password
        self.email = email

    def sign_in(self):
        print(f'Hello, {self.user}. You are logged in')


s = Singleton('Bohdan', '12345', 'bodya@gmail.com')
s1 = Singleton('Don', '67890', 'don@gmail.com')
print(s is s1)
