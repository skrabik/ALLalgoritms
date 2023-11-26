n = int(input())
matrix = [None for i in range(n)]
min_distanse = [0 for i in range(n)]
curent_distanse = 0
import math

if n == 1:
    print(0)
    exit()

for i in range(n):
    matrix[i] = [int(i) for i in input().split()]
    g = set(matrix[i])
    g.remove(0)
    g = min(g)
    min_distanse[i] = g
    curent_distanse += g
min_rast = math.inf
searched = [0]
min_rast = 0
while len(searched) != n:
    mn_ind = 0
    plus = math.inf
    for i in range(n):
        if i not in searched:
            if matrix[searched[-1]][i] < plus and matrix[searched[-1]][i] > 0:
                mn_ind = i
                plus = matrix[searched[-1]][i]
    # print(plus, mn_ind)
    searched.append(mn_ind)
    min_rast += plus
min_rast += matrix[searched[-1]][0]
print(searched)
print(min_rast)

count = 0
def get_optimal_route(n, searched = [0], rast=0):
    global curent_distanse
    global min_rast
    global count
    count += 1
    if len(searched) == n:
        if matrix[searched[-1]][0] != 0:
            rast += matrix[searched[-1]][0]
            if rast < min_rast:
                min_rast = rast
        return
    for i in range(1, n):
        if i not in searched:
            el = matrix[searched[-1]][i]
            if el == 0:
                continue
            rast += el
            curent_distanse -= min_distanse[i]
            if min_rast <= rast + curent_distanse:
                return
            searched.append(i)
            get_optimal_route(n, searched, rast)
            rast -= el
            curent_distanse += min_distanse[i]
            searched.pop()

get_optimal_route(n)
print(count)
if min_rast == math.inf:
    print(-1)
else:
    print(min_rast)