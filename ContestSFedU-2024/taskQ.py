# как же мне надоела эта хуета ебаная
import math

N = int(input())

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def in_line(X, T):
    x, y = X
    l1, l2 = T
    xl1, yl1 = l1
    xl2, yl2 = l2

    d1 = distance(x, y, xl2, yl2)
    d2 = distance(x, y, xl1, yl1)
    d3 = distance(xl1, yl1, xl2, yl2)
    if round(abs(d1) + abs(d2), 7) == round(abs(d3), 7):
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
    # if xh2 == 0 and xh4 == 0:
    #     parallel = True
    # elif yh2 == 0 and yh4 == 0:
    #     parallel = True
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

def one_pol(t1, t2, l1, l2):
    lx1, ly1 = l1
    lx2, ly2 = l2

    x1, y1 = t1
    x2, y2 = t2


    a = ly1 - ly2
    b = lx2 - lx1
    c = (lx1*ly2) - (lx2*ly1)

    res1 = a*x1 + b*y1 + c
    res2 = a*x2 + b*y2 + c

    if res1*res2 < 0:
        return True
    elif res1*res2 > 0:
        return False
    return False

def in_treangle(i, t2):
    K1, K2, K3 = t2
    x0, y0 = i
    x1, y1 = K1
    x2, y2 = K2
    x3, y3 = K3
    v1 = ((x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0))
    v2 = ((x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0))
    v3 = ((x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0))
    if v1 >= 0 and v2 >= 0 and v3 >= 0:
        return True
    if v1 < 0 and v2 < 0 and v3 < 0:
        return True
    return False

data = []
for i in range(N):
    data.append(tuple(map(int, input().split())))
triangles = []
M = int(input())
for i in range(M):
    triangles.append(tuple(map(int, input().split())))

answer = True

all_S = 0
for i in triangles:
    a, b, c = i
    x1, y1 = data[a-1]
    x2, y2 = data[b-1]
    x3, y3 = data[c-1]
    S = 1/2*abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1))
    all_S += S
    if S == 0:
        answer = False
        break

S_rectangle = (data[1][1]) * (data[2][0])

if all_S != S_rectangle:
    answer = False

set_triangles = set()

for i in triangles:
    for j in i:
        set_triangles.add(data[j-1])

if set(data) != set_triangles:
    answer = False

for el1 in range(M):
    for el2 in range(M):
        if el1 != el2:
            first = triangles[el1]
            second = triangles[el2]

            t1 = [data[first[0]-1], data[first[1]-1], data[first[2]-1]]
            t2 = [data[second[0]-1], data[second[1]-1], data[second[2]-1]]

            common = set(t1) & set(t2)

            helper1 = {(t1[0], t1[1]), (t1[1], t1[2]), (t1[0], t1[2])}
            helper2 = {(t2[0], t2[1]), (t2[1], t2[2]), (t2[0], t2[2])}


            if len(common) == 0:
                for i in t1:
                    if in_treangle(i, t2):
                        answer = False
                for i in t2:
                    if in_treangle(i, t1):
                        answer = False


            count_per = 0
            if len(common) == 1:
                for i in helper1:
                    for j in helper2:
                        if intersection(i, j):
                            count_per += 1

                if count_per != 4:
                    answer = False
                    break

            count_per = 0
            if len(common) == 2:
                for i in helper1:
                    for j in helper2:
                        if intersection(i, j):
                            count_per += 1

                if count_per != 7:
                    answer = False
                    break

            if len(common) == 3:
                answer = False
                break

            if len(common) == 2:
                helper = list(set(t1 + t2) - common)
                common = list(common)
                l1, l2 = common[0], common[1]
                m1, m2 = helper[0], helper[1]
                if one_pol(m1, m2, l1, l2) == False:
                    answer = False
                    break


if answer:
    print('Yes')
else:
    print('No')