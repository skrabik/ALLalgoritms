def bynary_search(array, target):
    l = 0
    r = len(array)
    while l != r:
        mid = (l+r) // 2
        if mid == target:
            return mid
        elif target > array[mid]:
            l = mid + 1

        else:
            r = mid
    return r

