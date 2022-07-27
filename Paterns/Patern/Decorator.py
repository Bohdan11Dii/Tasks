# def decorator_multiplu(func):
#     def multiplu(self):
#         return func(self)*5
#     return multiplu
#
#
# class DecoratorMultiplu:
#     def __init__(self,a, b):
#         self.a = a
#         self.b = b
#
#     @decorator_multiplu
#     def add_integer(self):
#         return self.a + self.b
#
#
# d = DecoratorMultiplu(10, 23)
# print(d.add_integer())
import datetime


class Time:
    def _decorator(func):
        def times_work(work):
            print(f'Registration in {datetime.datetime.now()}')
            func(work)
        return times_work


class Work:
    def __init__(self, username, lastname):
        self.username = username
        self.lastname = lastname

    @Time._decorator
    def registration(self):
        print(f'Hello in our site {self.lastname} {self.username}')


w = Work('Bohdan', 'Brovdiy')
print(w.registration())

