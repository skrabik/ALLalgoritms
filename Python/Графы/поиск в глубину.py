# обход в глубину aka DFS

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

cache = []
searched = []

cache.append('you')
enter_order = []

while len(cache) != 0:
    el = cache[0]
    cache = cache[1:]
    enter_order.append(el)
    searched.append(el)
    for i in graph[el]:
       if i not in searched:
           cache.insert(0, i)
print(enter_order)

N = int(input())
grad = [None for i in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    grad[i] = (a, b)

# data = [[- 1 for i in range(N)] for i in range(N)]

data = {}

for i in range(N-1):
    a, b, c = map(int, input().split())
    if a-1 not in data:
        data[a-1] = [[b-1, c]]
    else:
        data[a-1].append([b-1, c])
    if b-1 not in data:
        data[b-1] = [[a-1, c]]
    else:
        data[b-1].append([a-1, c])
# print(data)


