N, K = map(int, input().split())

adj = [[] for i in range(N)]

for i in range(K):
    a, b, l = map(int, input().split())
    adj[a-1].append((b-1, l))
    adj[b-1].append((a-1, l))

import math

S, F = map(int, input().split())

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
    return adj[el]


while stack:
    el = stack[0]
    stack.pop()
    rassm.add(el)

    all_ver = get_all_ver(el, rassm)

    for i in all_ver:
        if ver[i[0]] > ver[el] + i[1]:
            ver[i[0]] = i[1] + ver[el]

    next = get_next_ver(ver, rassm)


    if next != None:
        stack.append(next)

if ver[F-1] == math.inf:
    print(-1)
else:
    print(ver[F-1])
