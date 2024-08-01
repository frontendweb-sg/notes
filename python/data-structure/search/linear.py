array: list[int] = [1, 5, 7, 2, 9, 10, 44, 22, 33, 46]


def lSearch(array: list[int], item: int):
    length = len(array)
    print(length, array)
    for i in range(length):
        if (array[i] == item):
            print(f"i={i}")
            return i
    return -1


print(lSearch(array, 10))
