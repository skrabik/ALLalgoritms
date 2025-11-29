p, m, c = map(int, input().split())

all_peoples = (p + m)

free_peoples = all_peoples - c 

mozno_using = (free_peoples // 3)
if p // 2 < mozno_using:
    mozno_using = p // 2
if m < mozno_using:
    mozno_using = m
print(mozno_using)
