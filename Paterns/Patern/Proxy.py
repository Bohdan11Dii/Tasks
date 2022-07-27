import logging


class Concatenation:
    def concatenation(self, username, userlastname):
        return username + ' ' + userlastname


class Proxy:
    def __init__(self):
        self._add = Concatenation()

    def concatenation(self, username, userlastname):
        try:
            result = self._add.concatenation(username, userlastname)
            return result
        except TypeError:
            logging.error('Argument must be string')

p = Proxy()
print(p.concatenation('Bohdan', 2))