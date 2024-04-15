a, b = map(int, input().split())

helper = [0, 1, 4, 9, 6, 5, 6, 9, 4, 1]
helper = helper + helper + helper

razn = abs(b-a+1)
res = 0

if (razn // 10) % 2 == 1:
    res = 5
t = (razn % 10)

start = a % 10

for i in range(start, start+t):
    res += helper[i]
print(res%10)