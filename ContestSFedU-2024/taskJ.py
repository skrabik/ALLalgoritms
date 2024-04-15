n = int(input())
data = [int(i) for i in input().split()]
data.sort()
res = 0
for i in range(n):
    res += abs(data[i] - data[-1-i])
print(res)