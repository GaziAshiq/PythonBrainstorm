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

value = 4.5  # this will raise a warning


# let's use it in a function
def format_value(user_input: str | int | float) -> str:
    return str(user_input)


print(f'format value: {format_value(10)} , type: {type(format_value(10))}')
print(f'format value: {format_value(5.6)}, type: {type(format_value(5.6))}')
print(f'format value: {format_value("hi")} , type: {type(format_value("hi"))}')
# endregion

# region: List Type Annotations
# let's define a list
numbers: list = [1, 2, 3, 4, 5] # OK
numbers = (1, 2, 3, 4, 5)  # this will raise a warning, because we are changing to tuple

# let's define a list of integers
elements: list[int] = [1, 2, 3, 4, 5] # OK
elements = [1.0, 2.0, 'a', 'b']  # this will raise a warning

# let's define a list of strings and integers
values: list[str | int] = [1, 'a', 2, 'b'] # OK

# nested list
nested_list: list[list[int]] = [[1, 2], [3, 4], [5, 6]] # OK
# endregion


