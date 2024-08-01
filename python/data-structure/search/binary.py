"""
Binary Search:

Binary search works only sorted arrays.

Steps:
1. Find the middle index of the array.
2. Compare the middle element with the target element.
3. If the middle element is equal to the target, return the index.
4. If the middle element is greater than the target, search in the left half of the array.
5. If the middle element is smaller than the target, search in the right half of the array.

Time complexity:
    Best case: O(1) when the target is found at the middle index.
    Average case: O(log n) in the best and average cases.
    Worst case: O(log n) in the worst case when the target is not found.

Space complexity: 
    O(1) since it does not use any additional data structures.
    
"""


def binarySearch(array: list[int], target: int):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

# Example usage:


array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13

result = binarySearch(array, target)
if result != -1:
    print(f"Target found at index {result}")
    print(f"Element at index {result} is: {array[result]}")
    print("Array before swapping:")
    print(array)
    array[result], array[result+1] = array[result+1], array[result]
    print("Array after swapping:")
    print(array)
