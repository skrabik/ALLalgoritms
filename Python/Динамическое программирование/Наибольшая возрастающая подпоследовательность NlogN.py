# задача
# Найти длину самой большой возрастающей подпоследовательности в массиве

# https://habr.com/ru/articles/343210/

n, a1, k, b, m = map(int, input().split())
data = [0 for i in range(n)]
data[0] = a1
  
for i in range(1, n):
    data[i] = (k*data[i-1] + b) % m

max_subsquense = list()
indexes = [0 for _ in range(n)]

def get_index(subsequense, element):
    # for i in range(len(subsequense)):
    #     if element <= subsequense[i]:
    #         return i

    l, r = 0, len(subsequense)-1
    while r - l > 1:
        mid = (l + r) // 2
        if subsequense[mid] > element:
            r = mid
        else:
            l = mid
    if element <= subsequense[l]:
        return l
    return r


for i in range(len(data)):
    if len(max_subsquense) == 0:
        max_subsquense.append(data[i])
        indexes[i] = 0
    else:
        if data[i] > max_subsquense[-1]:
            indexes[i] = len(max_subsquense)
            max_subsquense.append(data[i])
        else:
            ind = get_index(max_subsquense, data[i])
            max_subsquense[ind] = data[i]
            indexes[i] = ind

res = list()
mx = max(indexes)
for i in range(len(data)-1, -1, -1):
    if indexes[i] == mx:
        res.append(data[i])
        mx -= 1
 
for i in range(len(res)-1, -1, -1):
    print(res[i], end=' ')


