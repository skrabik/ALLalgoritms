from datetime import time, timedelta

n = int(input())
f = timedelta(hours=int(0), minutes=int(0))
for _ in range(n):
    h, m = input().split(':')
    d = timedelta(hours=int(h), minutes=int(m))
    f += d
u = timedelta(hours=int(12), minutes=int(00))
if f >= u:
    f -= u
f = str(f)[:-3]
if len(f) < 5:
    print('0' + f)
else:
    print(f)