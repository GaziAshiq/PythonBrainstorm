class Car:
    """
    A class to represent a car.

    Attributes:
        name (str): The name of the car.
        color (str): The color of the car.
    """

    def __init__(self, name, color):
        """
        Constructs all the necessary attributes for the car object.

        Args:
            name (str): The name of the car.
            color (str): The color of the car.
        """
        self.name = name
        self.color = color

    def start(self):
        """
        Prints a message indicating that the car has started.
        """
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
