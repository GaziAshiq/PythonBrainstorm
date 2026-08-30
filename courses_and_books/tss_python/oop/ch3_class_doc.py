class Car:
    """
    A class to represent a car.

    Attributes:
        name (str): The name of the car.
        color (str): The color of the car.
    """

    # Class attributes
    a = ''  # most of the time, class attributes aren't needed

    # Constructor (special method used to initialize the object)
    def __init__(self, name, color):
        # Instance attributes (unique to each instance)
        self.name = name
        self.color = color

    # Instance method
    def start(self):
        print('starting')


# Create an instance of Car with name 'bmw' and color 'white'
my = Car('bmw', 'white')
print(my.name)
my.start()

# Create another instance of Car with name 'yamaha' and color 'blue'
new = Car('yamaha', 'blue')
# Add a new attribute 'year' to the new instance
new.year = 2019
print(new.name, new.color, new.year)
