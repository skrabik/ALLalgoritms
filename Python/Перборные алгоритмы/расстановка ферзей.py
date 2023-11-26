n = int(input())

count = 0
def queens(n, breaking_column = []):
    global count
    S = set()
    for i in range(len(breaking_column)):
        if (i - breaking_column[i]) in S:
            return
        S.add((i - breaking_column[i]))
    S = set()
    for i in range(len(breaking_column)):
        if (i + breaking_column[i]) in S:
            return
        S.add((i + breaking_column[i]))
    if len(breaking_column) == n:
        count += 1
        return
    for i in range(n): # 0 1 2
        if i not in breaking_column:
            breaking_column.append(i)
            queens(n, breaking_column) # 1 2
            # print(breaking_column)
            breaking_column.pop()
queens(n)
print(count)









