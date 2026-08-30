class Vehicle:
    """Base class for all vehicle"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving → ", self.manufacturer, self.name)

    def turn(self):
        print("Turning", self.name, 'to', direction)

    def brake(self):
        print(self.name, 'is stopping!')


class Car(Vehicle):
    """Car class"""

    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.wheels = 4
        print("This", self.name, " car has arrived")
        print("This car has ", self.wheels, "wheels")
        print("This car was build in ", self.year)

    def change_gear(self, gear_name):
        """method of changing gears"""

        print(self.name, "is changing gear to", gear_name)

if __name__ == "__main__":
    c = Car('Accord', 'Honda', 'Silver', 2015)

