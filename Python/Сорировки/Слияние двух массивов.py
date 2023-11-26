def merge(arr1, arr2, n, m):
    rezult = [None]* (n+m)

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

n = int(input())
arr1 = [int(i) for i in input().split()]
m = int(input())
arr2 = [int(i) for i in input().split()]

if n == 0 and m == 0:
    print('')
elif n == 0:
    print(" ".join(list(map(str, arr2))))
elif m == 0:
    print(" ".join(list(map(str, arr1))))
else:
    print(" ".join(list(map(str, merge(arr1, arr2, n, m)))))



