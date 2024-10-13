#
#dp[i][j] = max(data[i]-dp[i-1][j], data[j]-dp[i][j+1])
#https://www.youtube.com/watch?v=pzUMwIjMFso&t=1009s
#


n = int(input())
data = [int(i) for i in input().split()]
dp = [[0 for i in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = data[i]

for i in range(1, n):
    for j in range(i-1, -1, -1):
        # print(i, j)
        dp[i][j] = max(data[i]-dp[i-1][j], data[j]-dp[i][j+1])


res = dp[n-1][0]
if res > 0:
    print(1)
elif res < 0:
    print(2)
else:
    print(0)