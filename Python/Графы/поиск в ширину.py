# обход в ширину aka BFS

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

for i in graph['you']:
    cache.append(i)

while len(cache) != 0:
    print(cache)
    if cache[0] == 'jonny':
        print(cache[0])
        break
    else:
        for i in graph[cache[0]]:
            if i not in searched:
                cache.append(i)
            searched.append(i)
        cache = cache[1:]