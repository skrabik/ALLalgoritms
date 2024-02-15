#
# Рабочий вариант!!!
#

def binary_search(data, target):
    if len(data) == 0:
        return 0
    if target > data[-1]:
        return len(data)
    l = 0
    r = len(data) - 1
    while l < r:
        mid = (l + r) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            l = mid + 1
        else:
            r = mid
    return r

