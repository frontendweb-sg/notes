def counter(n: int):
    for x in range(n):
        yield x


print(next(counter(5)))
