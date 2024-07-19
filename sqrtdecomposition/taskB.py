from math import sqrt, ceil

n, m = map(int, input().split())

data = [int(i) for i in input().split()]

nblock = ceil(sqrt(len(data)))
decomposition = []
for i in range(0, len(data), nblock):
    mn = min(data[i:min(len(data), i+nblock)])
    cnt = data[i:min(len(data), i+nblock)].count(mn)
    decomposition.append([mn, cnt])

def update(ind, val):
    prev, data[ind] = data[ind], val
    mn = min(data[(ind//nblock)*nblock:((ind//nblock)*nblock)+nblock])
    cnt = data[(ind//nblock)*nblock:((ind//nblock)*nblock)+nblock].count(mn)
    decomposition[ind//nblock][0] = mn
    decomposition[ind//nblock][1] = cnt
def get_min(l, r):
    lsqrt = l // nblock
    rsqrt = r // nblock

    if lsqrt >= rsqrt:
        return min(data[l:r])
    sr = []
    if lsqrt+1 < rsqrt:
        sr.append(min(decomposition[lsqrt+1:rsqrt]))
    if l < (lsqrt + 1)*nblock:
        sr.append(min(data[l:(lsqrt + 1)*nblock]))
    if rsqrt*nblock < r:
        sr.append(min(data[rsqrt*nblock:r]))

    return min(sr)

for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        update(b, c)
    else:
        print(get_min(b, c))







