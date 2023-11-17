def merge(arr1, arr2):

    n = len(arr1)
    m = len(arr2)

    rezult = [None] * (n + m)

    a = 0
    b = 0

    for i in range(n + m):
        if arr1[a] <= arr2[b]:
            rezult[i] = arr1[a]
            a += 1
        else:
            rezult[i] = arr2[b]
            b += 1
        if a == n:
            for c in range(i+1, n + m):
                rezult[c] = arr2[b]
                b += 1
            break
        if b == m:
            for c in range(i+1, n + m):
                rezult[c] = arr1[a]
                a += 1
            break
    return rezult
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    elif len(arr) == 1:
        return merge(arr[0], arr[1])

    r = arr[len(arr) // 2:]
    l = arr[:len(arr) // 2]

    return merge(merge_sort(l), merge_sort(r))

n = int(input())
data = [int(i) for i in input().split()]
if n == 0:
    print('')
else:
    print(" ".join(list(map(str, merge_sort(data)))))



