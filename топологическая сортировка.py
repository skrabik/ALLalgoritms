# обход в глубину aka DFS

graph = [(0, 1, 0, 1, 0),
         (0, 0, 1, 0, 0),
         (0, 0, 0, 0, 1),
         (0, 0, 1, 0, 1),
         (0, 0, 0, 0, 0)]

cache = []
cache.append(0)

red = []
x = 1
while len(cache) > 0:
    flag = True
    el = cache[0]
    # print(el,'el')
    for i in range(len(graph)):
        if graph[el][i] == 1 and (i not in red):
            flag = False
            cache.insert(0, i)

    if flag:
        red.append(el)
        # print(red)
        cache.pop(0)
    # print(cache)
    # x += 1
    # if x == 5:
    #     break
print(red)






