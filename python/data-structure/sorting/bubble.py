arr: list[int] = [5, 4, 2, 3, 1, 9, 6]

# Bubble sort


def bubbleSort(arr: list[int]):
    """Bubble sort"""
    for i, v in enumerate(arr):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


if __name__ == '__main__':
    print(arr)
    bubbleSort(arr)
    print(arr)
