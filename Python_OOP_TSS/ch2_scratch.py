import builtins
import math
from datetime import date, datetime, timedelta

# region Module: math
# Print a list of all built-in functions and variables
print(dir(builtins))

# Print the value of pi
print(math.pi)

# Print x raised to the power of y
print(math.pow(2, 3))

# Print the square root of x
print(math.sqrt(25))

# Print the floor value of x
print(math.floor(5.2))

# Print the ceiling value of x
print(math.ceil(5.2))

# Print the absolute value of x
print(abs(-5))

# Print the maximum value from a list of numbers
print(max(1, 2, 3, 4, 5))

# Print the minimum value from a list of numbers
print(min(1, 2, 3, 4, 5))

# Print the sum of a list of numbers
print(sum([1, 2, 3, 4, 5]))

# Print the factorial of x
print(math.factorial(5))
# endregion


# region Module: date and time
# Use case 1: Get today's date
today = date.today()
print("Today's date:", today)

# Use case 2: Get the current date and time
now = datetime.now()
print("Current date and time:", now)

# Use case 3: Create a specific date
specific_date = date(2023, 10, 1)
print("Specific date:", specific_date)

# Use case 4: Create a specific date and time
specific_datetime = datetime(2023, 10, 1, 14, 30, 0)
print("Specific date and time:", specific_datetime)

# Use case 5: Calculate the difference between two dates
date1 = date(2023, 10, 1)
date2 = date(2024, 10, 1)
difference = date2 - date1
print("Difference between dates:", difference.days, "days")

# Use case 6: Add or subtract days from a date
new_date = today + timedelta(days=10)
print("Date after 10 days:", new_date)

# Use case 7: Format a date as a string
formatted_date = today.strftime("%m-%d-%Y")
print("Formatted date:", formatted_date)

# Use case 8: Parse a date string into a date object
date_string = "2023-10-01"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d").date()
print("Parsed date:", parsed_date)

# Use case 9: Get the day of the week
day_of_week = today.strftime("%A")
print("Day of the week:", day_of_week)

# Use case 10: Get the current time
current_time = datetime.now().time()
print("Current time:", current_time)
# endregion
