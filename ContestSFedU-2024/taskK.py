n = int(input())
data = [int(i) for i in input().split()]
data = data[::-1]
data[0] = 0

print(data)
for i in range(1, n):
    last = max(0, i - data[i])

    data[i] = min(data[last], data[i-1]) + 1

print(data[-1])