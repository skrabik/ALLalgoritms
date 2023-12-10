t = int(input())

def get_sum_srt(s):
    rez = 0
    for i in s:
        rez += int(i)
    return rez


for i in range(t):
    data = [i for i in input().split()]
    d = {i: [0] for i in range(1, 6)}
    print(d)
    for i in data:
        d



