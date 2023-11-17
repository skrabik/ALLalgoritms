import math
import heapq

N, K = map(int, input().split())

adj = [[] for i in range(N)]

for i in range(K):
    a, b, l = map(int, input().split())
    adj[a-1].append((b-1, l))
    adj[b-1].append((a-1, l))

S, F = map(int, input().split())

start = S - 1


rassm = set()

stack = []
stack.append(start)

ver = [math.inf for _ in range(N)]
ver[start] = 0

H = [[ver[i], i] for i in range(N)]
heapq.heapify(H)


while stack:
    el = stack[0]
    stack.pop()
    rassm.add(el)

    all_ver = adj[el]

    for i in all_ver:
        if i[0] not in rassm:
            if ver[i[0]] > ver[el] + i[1]:
                heapq.heappush(H, [i[1] + ver[el], i[0]])
                ver[i[0]] = i[1] + ver[el]

    while len(H) > 0:
        next = heapq.heappop(H)[1]
        if next not in rassm:
            stack.append(next)
            break

if ver[F-1] == math.inf:
    print(-1)
else:
    print(ver[F-1])