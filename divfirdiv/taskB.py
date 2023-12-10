t = int(input())

def im(): return list(map(int, input().split()))

for i in range(t):
    n = int(input())
    data = im()
    data.sort()
    rez = 0
    cords = []
    for i in range(n):
        cords.append([data[i], data[-1-i]])
    for i in range(1, len(cords)):
        rez += abs(cords[i][0] - cords[i-1][0])
        rez += abs(cords[i][1] - cords[i-1][1])
    print(rez)
    for a, b in cords:
        print(a, b)
