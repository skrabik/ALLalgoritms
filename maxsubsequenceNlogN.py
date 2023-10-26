# задача
# Найти длину самой большой возрастающей подпоследовательности в массиве
def bynary_search(array, target):
    l = 0
    r = len(array)
    while l != r:
        mid = (l+r) // 2
        if mid == target:
            return mid
        elif target > array[mid]:
            l = mid + 1

        else:
            r = mid
    return r
n = 8
data = [5, 10, 6, 12, 3, 24, 7, 8]
subsequence = []
indexes = [0]*len(data)
subsequence.append(data[0])
max_length = -1
for i in range(1, n):
    ind = bynary_search(subsequence, data[i])
    indexes[i] = ind
    if data[i] > subsequence[-1]:
        subsequence.append(data[i])
    else:
        ind = bynary_search(subsequence, data[i])
        subsequence[ind] = data[i]

    max_length = max(max_length, indexes[i])
print(max(indexes)+1)
print(subsequence)

# https://habr.com/ru/articles/343210/





