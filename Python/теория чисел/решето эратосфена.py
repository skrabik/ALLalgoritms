# это алгоритм, позволяющий найти все простые числа из отрезка [1, n] за NloglogN

# моя реализация
n = 100
data = [[True, i] for i in range(n)]

for i in range(2, n):
    if data[i][0]:
        for j in range(i*2, n, i):
            data[j][0] = False

# print(data)
res = [b for a, b in data if a]
print(res)

# чужая реализация
# n = int(input())
n = 10
numbers = [i for i in range(n+1)]

numbers[1] = 0

i = 2

while i < n:
    if numbers[i] != 0:
        j = i + i
        while j <= n:
            numbers[j] = 0
            j = j + i
    i += 1

result = [i for i in numbers if i != 0]
# print(result)
# print(numbers)

# можем находить для каждого числа простой делитель
# https://www.youtube.com/watch?v=dF04ZBU1Jdo
# *можно так разложить на простые делители за логарифм
# количество делителей/простых делителей


