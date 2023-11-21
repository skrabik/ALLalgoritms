data = [-2, -3, 4, -1, -2, 5, -3]

mx_end = 0
mx_till = 0

for i in range(len(data)):
    mx_end = mx_end + data[i]
    if mx_end < 0:
        mx_end = 0
    elif mx_end > mx_till:
        mx_till = mx_end

print(mx_till)

n = int(input())
data = list(map(int, input().split()))
dp = [-10**9 for i in range(n)]
mx = 0
answer = -10**9
for i in range(n):
    if i-1 >= 0 and data[i] % 2 != data[i-1] % 2:
        dp[i] = dp[i-1] + data[i]
    dp[i] = max(dp[i], data[i])
    answer = max(answer, dp[i])

print(answer)