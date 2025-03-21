k = int(input())

n = 10**9 + 100
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

result = {i for i in numbers if i != 0}

for _ in range(k):
    n = int(input)
    if n in numbers:
        print("YES")
    else:
        print("NO")