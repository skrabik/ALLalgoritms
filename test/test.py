def get_column(data, j):
    res = list()
    for i in range(3):
        res.append(data[i][j])
    return res

def check(data):
    data = [[data[i], data[i+1], data[i+2]] for i in (0, 3, 6)]
    for i in range(3):
        if sum(data[i]) != 15:
            return False
        if sum(get_column(data, i)) != 15:
            return False
    if (data[0][0] + data[1][1] + data[2][2]) != 15:
        return False
    if (data[1][1] + data[0][2] + data[2][0]) != 15:
            return False
    return True

res = list()
def recursion(data = []):
    if len(data) == 9:
        if check(data):
            res.append(data)
    for el in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if el not in data:
            recursion(data + [el])

recursion()

def question(i, j):
    print(i, j, flush=True)
    answer = int(input())
    return answer

a = question(1, 2)
b = question(2, 1)
flag = False
if a in (9, 7, 3, 1) and b in (9, 7, 3, 1):
    pass
else:
    if b in (9, 7, 3, 1):
        b, a = a, b
        flag = True
    if a == 9:
        if b in (8, 6):
            b = 7
        else:
            b = 3
    if a == 7:
        if b == 2:
            b = 1 
        else:
            b = 9
    if a == 3:
        if b == 2:
            b = 1
        else:
            b = 9
    if a == 1:
        if b in (6, 8):
            b = 7
        else:
            b = 3
    if flag:
        a, b = b, a


for data in res:
    helper = [[data[i], data[i+1], data[i+2]] for i in (0, 3, 6)]
    if helper[0][1] == a and helper[1][0] == b:
        print(*data, sep='')
        break