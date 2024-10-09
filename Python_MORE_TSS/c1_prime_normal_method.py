def is_prime(n):
    """
      The function first handles the edge cases where `n` is less than or equal to 1, or exactly 2.
      Then, it checks if `n` is even, returning False for even numbers greater than 2.
      For odd numbers greater than 2, it checks divisibility by odd numbers up to the square root of `n`.
      If `n` is divisible by any of these, it is not prime.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = int(n ** 0.5)

    for i in range(3, root + 1, 2):
        if n % i == 0:
            print(f'{n} divisible by {i}')
            return False

    return True


def gen_prime(n, m):
    primes = list()

    i = 0
    while i < m:
        if is_prime(n):
            primes.append(n)
            i += 1
        n += 1
    return primes


if __name__ == "__main__":
    primes = gen_prime(2, 20)
    sum_primes = sum(primes)
    print("sum: ", sum_primes)