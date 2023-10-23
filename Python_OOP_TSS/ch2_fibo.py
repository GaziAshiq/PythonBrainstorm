def fibo(n):
	if n <= 2:
		return 1

	fibo_x, fibo_next = 1, 1

	i = 3
	while i <= n:
		i += 1
		fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
	return fibo_next


def fibo_list(n):
	li_fib = []

	if n == 1:
		li_fib.append(1)
	elif n==2:
		li_fib.append(1)
		li_fib.append(1)
	else:
		fibo_x, fibo_next = 1,1
		li_fib.append(fibo_x)
		li_fib.append(fibo_next)

		for i in range(2, n):
			fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
			li_fib.append(fibo_next)

	return li_fib


if __name__ == "__main__":
	for i in range(1, 11):
		print(fibo(i))
	print(fibo_list(10))
