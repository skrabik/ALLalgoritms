def bynary_search(array, target):
    l = 0
    r = len(array) - 1
    while l <= r:
        mid = (l+r) // 2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            l = mid + 1

        else:
            r = mid
    return -1


print(bynary_search([1,2,3,4,5], 3))