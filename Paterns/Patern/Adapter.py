class Windows:
    def __init__(self, name):
        self.name = name

    def connect_wifi_in_windows(self):
        print(f'Wifi connected in {self.name}')


class Linux:
    def __init__(self, name):
        self.name = name

    def connect_wifi_in_linux(self):
        print(f'Wifi connected {self.name}')


class Wifi:
    def __init__(self, work):
        self.work = work

    def connect(self):
        self.work.connect_wifi_in_windows()


class Adapter:
    def __init__(self):
        self.linux = Linux("Ubuntu")

    def connect_wifi_in_windows(self):
        self.linux.connect_wifi_in_linux()


def menu():
    win = Windows('Windows 11')
    wifi = Wifi(win)
    wifi.connect()

    ad = Adapter()
    wifi = Wifi(ad)
    wifi.connect()






menu()