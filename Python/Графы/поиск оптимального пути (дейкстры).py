import math

N, S, F = map(int, input().split())

matrix = [[None] for _ in range(N)]

for i in range(N):
    matrix[i] = list(map(int, input().split()))


start = S - 1

rassm = set()

stack = []
stack.append(start)

ver = [math.inf for _ in range(N)]
ver[start] = 0

def get_next_ver(ver, rassm):
    mn = math.inf
    rez = None
    for i in range(len(ver)):
        if i not in rassm:
            if ver[i] < mn:
                mn = ver[i]
                rez = i
    return rez

def get_all_ver(el, rassm):
    rez = []
    for i in range(len(matrix[el])):
        if i not in rassm and matrix[el][i] > 0:
            rez.append((i, matrix[el][i]))
    return rez


M = [0]*N
while stack:
    el = stack[0]
    stack.pop()
    rassm.add(el)

    all_ver = get_all_ver(el, rassm)

    for i in all_ver:
        if ver[i[0]] > ver[el] + i[1]:
            ver[i[0]] = i[1] + ver[el]
            M[el] = i[0]

    next = get_next_ver(ver, rassm)


    if next != None:
        stack.append(next)

def get_all_ver2(el, rassm):
    rez = []
    for i in range(len(matrix[el])):
        if i not in rassm and matrix[i][el] > 0:
            rez.append((i, matrix[i][el]))
    return rez

start = F - 1

rassm = set()

stack = []
stack.append(start)

ver2 = [math.inf for _ in range(N)]
ver2[start] = 0

M = [0]*N
while stack:
    el = stack[0]
    stack.pop()
    rassm.add(el)

    all_ver = get_all_ver2(el, rassm)

    for i in all_ver:
        if ver2[i[0]] > ver2[el] + i[1]:
            ver2[i[0]] = i[1] + ver2[el]
            M[el] = i[0]

    next = get_next_ver(ver2, rassm)


    if next != None:
        stack.append(next)

def get_all(el):
    rez = []
    for i in range(len(matrix)):
        if matrix[el][i] > 0:
            rez.append(i)
    return rez


if ver[F-1] == math.inf:
    print(-1)
else:
    krat = ver[F - 1]
    start = S - 1
    d = start
    answer = [start+1]
    while d != (F - 1):
        for i in get_all(d):
            if ver[i] + ver2[i] == krat and matrix[d][i] + ver[d] + ver2[i] == krat:
                d = i
                answer.append(d + 1)
                break
    print(*answer, sep=' ')


