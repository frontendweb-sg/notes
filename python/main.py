def MyRange(start: int, end: int):
    current = start
    while current < end:
        yield current
        current += 1
