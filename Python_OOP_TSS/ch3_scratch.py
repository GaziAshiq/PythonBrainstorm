class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print('starting')


my = Car('bmw', 'white')
print(my.name)
my.start()

new = Car('yamaha', 'blue')
new.year = 2019
print(new.name, new.color, new.year)
