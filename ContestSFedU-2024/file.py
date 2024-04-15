import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def in_line(X, T):
    l1, l2 = T
    xl1, yl1 = l1
    xl2, yl2 = l2
    x, y = X

    d1 = distance(x, y, xl2, yl2)
    d2 = distance(x, y, xl1, yl1)
    d3 = distance(xl1, yl1, xl2, yl2)
    if round(d1 + d2, 6) == round(d3, 6):
        return True
    return False

def one_pol2(t1, t2, l1, l2):
    x1, y1 = l1
    x2, y2 = l2

    x3, y3 = t1
    x4, y4 = t2

    xh2, yh2 = x2 - x1, y2 - y1
    xh4, yh4 = x4 - x3, y4 - y3

    parallel = False
    if xh2 * yh4 == xh4 * yh2:
        parallel = True
    if parallel:
        if in_line(l1, (t1, t2)) or in_line(l2, (t1, t2)):
            return True
        else:
            return False

    a = y1 - y2
    b = x2 - x1
    c = (x1*y2) - (x2*y1)

    res1 = a*x3 + b*y3 + c
    res2 = a*x4 + b*y4 + c


    if res1*res2 == 0:
        return True
    elif res1*res2 < 0:
        return True
    else:
        return False


def intersection(v1, v2):
    t1, t2 = v1
    t3, t4 = v2

    if one_pol2(t1, t2, t3, t4) and one_pol2(t3, t4, t1, t2):
        return True
    else:
        return False

v1 = ((2, 2), (1, 1))
v2 = ((-1, -1), (0, 0))

print(intersection(v1, v2))
