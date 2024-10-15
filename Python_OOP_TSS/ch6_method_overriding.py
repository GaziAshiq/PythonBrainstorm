class Vehicle:
    """
    Base class for all vehicles
    """

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def turn(self, direction):
        print(f'Turning {self.name} to {direction}')


class Car(Vehicle):
    """CLass: Car, Inherit: Vehicle class"""

    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.wheels = 4

    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(f'{self.name} changing gear to {gear_name}')

    # Overriding the turn method of Vehicle class in Car class
    def turn(self, direction):
        print(f'{self.name} is turning {direction}')


if __name__ == '__main__':
    v = Vehicle('MT-15', 'Yamaha', 'Blue')
    c = Car('Mustang', 'Ford', 'Red', 2017)

    v.turn('Right')
    c.turn('Right')
