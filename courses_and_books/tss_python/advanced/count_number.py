def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


if __name__ == "__main__":
    n = input("Enter a positive integer: ")
    try:
        n = int(n)
        if n > 0:
            print("The number of digits in {} is {}".format(n, count_digits(n)))
        else:
            print("Invalid input. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
