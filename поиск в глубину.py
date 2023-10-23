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
    print(cache)
print(enter_order)


