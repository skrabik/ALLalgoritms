n, x, y = map(int, input().split())

leg = (y-1)*2 + 1 + 2
hat = (x*2) + 2 + 4 - 1
res = leg+hat

answer = res + (8*(n-1))
print(answer)