n = int(input())

def line(x, y, a, c):
    b = y - c/a*x
    if x > 0 and a > 0:
        return None
    elif x < 0 and a < 0:
        return None
    return b



def f(x1, y1, x2, y2, a, b):
    if a == 0:
        if (x1>0 and x2>0) or (x1<0 and x2<0):
            return False
        t_per = line(x1, y1, x2 - x1, y2 - y1)
        if t_per == 0: return True
        if t_per > 0 and b < 0: return True
        if t_per < 0 and b > 0: return True
        else: return False
    v1 = line(x1, y1, a, b)
    v2 = line(x2, y2, a, b)
    if (v1 == None) and (v2 == None):
        return False
    if (v1 == None) and (v2 != None):
        v1 = line(x1, y1, x2 - x1, y2 - y1)
    elif (v2 == None) and (v1 != None):
        v2 = line(x2, y2, x1 - x2, y1 - y2)
    if (v1 == 0) or (v2 == 0) or (v1 > 0 and v2 < 0) or (v1 < 0 and v2 > 0):
        return True
    else:
        return False


res = 0
for _ in range(n):
    x1, y1, x2, y2, a, b = map(int, input().split())
    if f(x1, y1, x2, y2, a, b):
        res += 1
print(res)