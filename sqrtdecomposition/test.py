triangle = 100
c = [[1 for i in range(triangle)] for i in range(triangle)]

for i in range(1, triangle):
    for j in range(1, i):
        c[i][j] = c[i-1][j-1] + c[i-1][j]
n, k = map(int, input().split())

bits = []
while (n >> 1):
    bits.append(str(n%2))
    n >>= 1
bits.append('1')
bits.reverse()
res = 0

for i in range(8, 14):
    print(bin(i)[2:])


if bits.count('0') <= k:
    for i in range(1, len(bits)):
        if bits[i] == '1':
            res += bits[i:].count('0')
    res += c[bits.count('1')-1][k-bits.count('0')]

print(res)













