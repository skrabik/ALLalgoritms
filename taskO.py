t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    ans = ((b//2) - (a//2))
    if b % 2 == 1:
        ans += 1

    c = 1
    k = 2
    a -= 1
    while (c << k) <= b+100:
        ans += ((b // (c << k)) - (a // (c << k))) * (k - 1)
        ans -= ((b // (c << k)) - (a // (c << k))) * (k - 2)
        k += 1
    print(ans)
