# region: Basic Type Annotations

text: str = 'hello world'
print(f'text: {text}')

number: int = 32
print(f'number: {number}')

percent: float = 0.5
print(f'float: {percent}')

is_true: bool = True
print(f'bool: {is_true}')


def format_title(title: str) -> str:
    return title.title()


print(f'format title: {format_title("hello world")}')
# endregion

# region: Union Type Annotations
# assume it, this variable can accept either a string or an integer
value: str | int = 10
print(f'value: {value}')
value = 'hello'
print(f'value: {value}')

# value = 4.5  # this will raise a warning


# let's use it in a function
def format_value(user_input: str | int | float) -> str:
    return str(user_input)


print(f'format value: {format_value(10)} , type: {type(format_value(10))}')
print(f'format value: {format_value(5.6)}, type: {type(format_value(5.6))}')
print(f'format value: {format_value("hi")} , type: {type(format_value("hi"))}')
# endregion

# region: List Type Annotations
# let's define a list
numbers: list = [1, 2, 3, 4, 5]  # OK
# numbers = (1, 2, 3, 4, 5)  # this will raise a warning, because we are changing to tuple

# let's define a list of integers
elements: list[int] = [1, 2, 3, 4, 5]  # OK
# elements = [1.0, 2.0, 'a', 'b']  # this will raise a warning

# let's define a list of strings and integers
values: list[str | int] = [1, 'a', 2, 'b']  # OK

# nested list
nested_list: list[list[int]] = [[1, 2], [3, 4], [5, 6]]  # OK
# endregion

# region: Tuple Type Annotations
# let's define a tuple
person: tuple = ('John', 25, 'New York')  # OK
john: tuple[str, int, str] = ('John', 25, 'New York')  # OK
many_types: tuple[str | int | float, str | int | float] = ('John', 25)  # OK
many_types2: tuple[str, int, float, str, bool] = ('John', 25, 5.6, 'New York', True)  # OK

# let's define a tuple with optional values
optional: tuple[str, int, str, str | None] = ('John', 25, 'New York', None)  # OK
coordinates: tuple[int | str, ...] = (34, 'text', 45, 'text')  # take any number of elements, type int or str
# endregion

# region: Set Type Annotations
# let's define a set
my_set: set = {1, 2, 3, 4, 5}  # OK
letters: set[str] = {'a', 'b', 'c', 'd', 'e'}  # OK
mixed: set[str | int] = {'a', 1, 'b', 2}  # OK
test_mixed: set[str | int] = {'a', 1, 'b', 2, None}
# None should raise a warning, but ide wouldn't show it, so we will use mypy to check it
# endregion

# region: Dictionary Type Annotations
# let's define a dictionary
my_dict: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}  # OK


# function with dictionary
def print_it(some_dict: dict[int, str]):
    for val in some_dict.values():
        print(val.title())


example: dict[int, str] = {1: "ping", 2: "mario"}
print_it(example)
# endregion

# region: Optional Type Annotations
# optional type is a type that can be either the defined type or None
# let's define a variable with optional type
name: str | None = 'John'
print(f'name: {name}')
name = None
print(f'name: {name}')


# let's define a function with optional type
def greet(name: str | None):
    if name is None:
        print('Hello, Guest!')
    else:
        print(f'Hello, {name}!')


greet('John')
greet(None)


# endregion

# region: Class Annotations
# let's define a class
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# let's create an instance of the class
gazi: Person = Person('Gazi', 25)


# let's define a function with class type
def print_person(person: Person):
    print(f'Name: {person.name}, Age: {person.age}')


print_person(gazi)  # OK


# someone = 'John'
# print_person(someone)  # this will raise a warning

# it's also going to work on subclasses
class Student(Person):
    pass


student: Student = Student('abir', 25)
print_person(student)  # OK


# endregion

# region: return type annotations
# let's define a function with return
def add(a: int, b: int) -> int:
    return a + b


print(f'add: {add(5, 6)}')
# print(f'add: {add(5, 6.5)}')  # this will raise a


# let's define a function with return type as None
def say_hello(name: str) -> None:
    print(f'Hello, {name}!')


# multiple return types
def fetch_user(user_id: int) -> str | None:
    users: dict[int, str] = {1: 'John', 2: 'Doe'}
    return users.get(user_id)

print(fetch_user(1))
print(fetch_user(3))
# endregion

# region: External Libraries Type Annotations
# let's use the requests library
import requests
from requests import Response

def get_status_code(url: str) -> int:
    response: Response = requests.get(url) #
    return response.status_code

print(f'status code: {get_status_code("https://www.google.com")}')
# endregion
