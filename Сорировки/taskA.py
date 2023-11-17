N = int(input())
data = [int(i) for i in input().split()]
x = int(input())
count = 0
for i in range(N):
    if data[i] < x:
        count += 1
print(count)
print(N-count)