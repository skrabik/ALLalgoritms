# будем искать минимум на отрезке за корень из n

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

from math import sqrt

sq = int(sqrt(len(s)))

data = []
for i in range(0, len(s), sq):
    data.append(sum(s[i:i+sq]))

def get_sum(l, r):
    sm = 0
    if l % sq == 0:
        l = l // sq
    else:
        sm += sum(s[l:((l//sq)+1)*sq])
        l = (l // sq) + 1
    if r % sq == 0:
        r = r // sq
    else:
        sm += sum(s[(r // sq)*sq:r])
        r = r // sq

    sm += sum(data[l:r])
    return sm
lf = 10
rt = 23
print(sum(s[lf:rt]))
print(get_sum(lf, rt))