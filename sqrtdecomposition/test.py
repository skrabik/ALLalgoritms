n, k = map(int, input().split())

step = (n+1)/(n-k+1)

print(step, (len(bin(n))-3))