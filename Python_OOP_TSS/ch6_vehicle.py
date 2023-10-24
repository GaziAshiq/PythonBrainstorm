class Vehicle:
    """
    Base class for all vehicles
    """

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print(f'Driving {self.manufacturer} {self.name}')

    def turn(self, direction):
        print(f'Turning {self.name} to {direction}')

    def brake(self):
        print(f'{self.name} is stopping!')


if __name__ == '__main__':
    v1 = Vehicle('MT-15', 'Yamaha', 'Glossy Black')
    v2 = Vehicle('GSX-S150', 'Suzuki', 'Yellow')
    v3 = Vehicle('Hunter 350', 'Royal Enfield', 'Blue-White')

    v1.drive()
    v2.drive()
    v3.drive()

    v1.turn('right')
    v2.turn('left')

    v1.brake()
    v2.brake()
    v3.brake()
