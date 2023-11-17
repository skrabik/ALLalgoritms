# граф вводим в виде списка рёбер
n, m = [int(i) for i in input().split()] # количество вершин и рёбер
g = [[] for i in range(n)] # список смежности
colors = [0 for i in range(n)] # храним "цвета" вершин

for i in range(m):
    a, b = [int(i)-1 for i in input().split()]
    g[a].append(b)

def dfs(v):
    colors[v] = 1
    for u in g[v]:
        if colors[u] == 0:
            if dfs(u):
                return True
        elif colors[u] == 1:
            return True
    colors[v] = 2
    return False
result = False
for i in range(n):
    if dfs(i):
        result=True
        break
print(result)

# https://www.youtube.com/watch?v=CAC13fyBz_M&t=329s