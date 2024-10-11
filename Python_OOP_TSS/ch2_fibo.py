def fibo(n):
    """
    Calculate the nth Fibonacci number.

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 2:
        return 1

    fibo_x, fibo_next = 1, 1

    for _ in range(3, n + 1):
        fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
    return fibo_next


def fibo_list(n):
    """
    Generate a list of the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list containing the first n Fibonacci numbers.
    """
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    fibo_x, fibo_next = 1, 1
    li_fib = [fibo_x, fibo_next]

    for _ in range(2, n):
        fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
        li_fib.append(fibo_next)

    return li_fib


if __name__ == "__main__":
    """
    Main block to print the first 10 Fibonacci numbers and the list of the first 10 Fibonacci numbers.
    """
    for i in range(1, 11):
        print(fibo(i))
    print(fibo_list(10))