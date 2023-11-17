n = int(input())
data = []
for _ in range(n):
    data.append(input())

m = len(data[0])

print('Initial array:')
print(*data, sep=', ')
print('**********')


t = 1
for i in range(m - 1, -1, -1):
    print(f'Phase {t}')
    t += 1

    buckets = [[] for i in range(10)]

    for el in data:
        buckets[int(el[i])].append(el)

    f = 0
    for i in buckets:
        if len(i) == 0:
            print(f'Bucket {f}: ', end='')
            print('empty')
        else:
            print(f'Bucket {f}: ', end='')
            print(*i, sep=', ')
        f += 1
    data = []
    for j in buckets:
        for k in j:
            data.append(k)
    print('**********')
print('Sorted array:')
print(*data, sep=', ')


