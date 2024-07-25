triangle = 1000
c = [[1 for i in range(triangle)] for i in range(triangle)]

for i in range(1, triangle):
    for j in range(1, i):
        c[i][j] = c[i-1][j-1] + c[i-1][j]

