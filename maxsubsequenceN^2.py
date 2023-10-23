# задача
# Найти длину самой большой возрастающей подпоследовательности в массиве
n = 8
data = [5, 10, 6, 12, 3, 24, 7, 8]
counts = [1]*len(data)

for i in range(n):
    for j in range(i+1,n):
        if data[i] < data[j] and counts[i] >= counts[j]:
            counts[j] = counts[i] + 1
print(counts)

