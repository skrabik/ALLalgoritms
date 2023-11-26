n = int(input())
s = input()
n = len(s)
s2 = s[::-1]
s2 = ' ' + s2
s = ' ' + s
p = 10**9+7
x_ = 257
h = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
h[0] = ord(s[0]) % p
for i in range(1, n+1):
    h[i] = (h[i-1] * x_ + ord(s[i])) % p
    x[i] = (x[i-1] * x_) % p
h2 = [0] * (n + 1)
h2[0] = ord(s2[0]) % p
for i in range(1, n+1):
    h2[i] = (h2[i-1] * x_ + ord(s2[i])) % p
def isequal(from1, from2,  slen):
    return (
        (h[from1 + slen - 1] - h[from1 - 1] * x[slen]) % p ==
        (h2[from2 + slen - 1] - h2[from2 - 1] * x[slen]) % p
    )



answer = []
for i in range(1, n+1):
    from1 = 1
    from2 = n-i+1

    l = 0
    r = i

    while l <= r:
        mid = (l + r) // 2
        if isequal(from1, from2, mid):
            l = mid + 1
        else:
            r = mid - 1
    answer.append(r)
print(*answer, sep=' ')