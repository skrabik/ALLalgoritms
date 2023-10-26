# задача
# Найти длину самой большой возрастающей подпоследовательности в массиве
n = 8
data = [5, 10, 6, 12, 3, 24, 7, 8]
counts = [1]*len(data)

for i in range(n):
    for j in range(i+1,n):
        if data[i] < data[j] and counts[i] >= counts[j]:
            counts[j] = counts[i] + 1
# print(counts)


def gis(A):
    """Возвращает длину наибольшей возрастающей подпоследовательности """
    F = [0]*(len(A)+1)
    for i in range(1, len(A)+1):
        m = 0 #максимум
        for j in range(0, i):
            if A[i-1] > A[j-1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return max(*F)

print(gis(data))
