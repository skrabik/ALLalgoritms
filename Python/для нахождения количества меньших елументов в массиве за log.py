
def large_el_in_array(data, more):
    if len(data) == 0:
        return 0
    if more < data[0]:
        return len(data)
    l = 0
    r = len(data) - 1
    while l < r:
        mid = (l + r) // 2
        if data[mid] == more:
            while data[mid - 1] == more:
                mid -= 1
            return len(data) - mid
        if data[mid] < more:
            l = mid + 1
        else:
            r = mid
    return len(data) - r

def smallest_el_in_array(data, less):
    if len(data) == 0:
        return 0
    if less < data[0]:
        return 0
    if less > data[-1]:
        return len(data)
    l = 0
    r = len(data) - 1
    while l < r:
        mid = (l + r) // 2
        if data[mid] == less:
            while data[mid + 1] == less:
                mid += 1
            return mid + 1
        if data[mid] < less:
            l = mid + 1
        else:
            r = mid
    return r + 1

data = [1, 4, 7]
print(smallest_el_in_array(data, -1))




# доп с задачи

t = int(input())


def large_el_in_array(data, less):
    if len(data) == 0:
        return 0
    if less < data[0]:
        return 0
    if less > data[-1]:
        return len(data)
    l = 0
    r = len(data) - 1
    while l < r:
        mid = (l + r) // 2
        if data[mid] == less:
            while data[mid + 1] == less:
                mid += 1
            return mid
        if data[mid] < less:
            l = mid + 1
        else:
            r = mid
    return r

def smallest_el_in_array(data, less):
    if len(data) == 0:
        return 0
    if less < data[0]:
        return 0
    if less > data[-1]:
        return len(data)
    l = 0
    r = len(data) - 1
    while l < r:
        mid = (l + r) // 2
        if data[mid] == less:
            while data[mid + 1] == less:
                mid += 1
            return mid + 1
        if data[mid] < less:
            l = mid + 1
        else:
            r = mid
    return r + 1


for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    data = [arr[0]]
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            data.append(arr[i])
    res = 1
    for i in range(len(data)):
        res = max(res, smallest_el_in_array(data, data[i]) - large_el_in_array(data, data[i]+1 - n))
    print(res)
