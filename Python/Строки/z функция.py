s = input()
n = len(s)

p = 10**9+7
x_ = 257
h = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
s = ' ' + s

for i in range(1, n+1):
    h[i] = (h[i-1] * x_ + ord(s[i])) % p
    x[i] = (x[i-1] * x_) % p
def isequal(from1, from2, slen):
    return (
        (h[from1 + slen - 1] + h[from2 -1]*x[slen]) % p ==
        (h[from2 + slen -1] + h[from1 -1]*x[slen]) % p
    )
answer = []


for i in range(n):
    if i == 0:
        answer.append(0)
        continue

    l = 1
    r = n-i

    while l <= r:
        mid = (l + r) // 2
        if isequal(1, i+1, mid):
            l = mid + 1
        else:
            r = mid - 1
    answer.append(r)


print(*answer, sep=' ')


