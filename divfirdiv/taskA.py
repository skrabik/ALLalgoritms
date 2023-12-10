t = int(input())

for i in range(t):
    x, y, k = map(int, input().split())
    if y < x:
        print(x)
        continue
    if x + k == y:
        print(y)
        continue
    if x + k < y:
        print((x+k) + ((y-(x+k))*2))
        continue
    if x + k > y:
        print(y)
        continue
