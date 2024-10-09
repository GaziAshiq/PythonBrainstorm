def foo():
    x = 1
    yield x
    x += 1
    yield x
    x += 2
    yield x


if __name__:
     x = foo()
     print(next(x))
     print(next(x))
     print(next(x))
     print(next(x))
     print(next(x))
     print(next(x))
