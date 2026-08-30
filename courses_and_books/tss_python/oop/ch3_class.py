class Car:
    def __init__(self, name, manufacturer, color, year, cc):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.cc = cc

    def start(self):
        print(f'{self.name} engine starting')

    def brake(self):
        print(f'{self.name} is braking!')

    def drive(self):
        print(f'{self.name} driven by me')

    def turn(self):
        print('turn right or turn left')

    def change_gear(self):
        print(f'{self.name} is changing gear')


race_car = Car('Tenary 700', 'yamaha', 'black', 2019, 700)
race_car.start()
