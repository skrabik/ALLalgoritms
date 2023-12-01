def binary_search(array, target):
    l = 0
    r = len(array) - 1
    while l <= r:
        mid = (l + r) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(binary_search(arr, target))
