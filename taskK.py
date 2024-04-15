def one_pol2(t1, t2, l1, l2):
    lx1, ly1 = l1
    lx2, ly2 = l2

    x1, y1 = t1
    x2, y2 = t2

    a = ly1 - ly2
    b = lx2 - lx1
    c = (lx1*ly2) - (lx2*ly1)

    res1 = a*x1 + b*y1 + c
    res2 = a*x2 + b*y2 + c


    if res1*res2 == 0:
        return True
    elif res1*res2 < 0:
        return True
    else:
        return False


def intersection(t1, t2, t3, t4):
    if one_pol2(t1, t2, t3, t4) and one_pol2(t3, t4, t1, t2):
        return True
    else:
        return False

t1 = (0, 0)
t2 = (1, 2)
t3 = (0, 3)
t4 = (1, 1)

# print(one_pol(t1, t2, t3, t4))
print(intersection(t1, t2, t3, t4))