import random

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[random.randint(0, len(arr)-1)]
    r = []
    l = []
    e = []
    for i in arr:
        if i < pivot:
            l.append(i)
        elif i > pivot:
            r.append(i)
        else:
            e.append(i)
    return quick_sort(l) + e + quick_sort(r)

N = int(input())
if N == 0:
    print('')
else:
    data = [int(i) for i in input().split()]
    print(" ".join(list(map(str, quick_sort(data)))))

