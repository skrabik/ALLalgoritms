from math import sqrt, ceil

n, m = map(int, input().split())

data = [int(i) for i in input().split()]

nblock = ceil(sqrt(len(data)))
decomposition = []
for i in range(0, len(data), nblock):
    decomposition.append(sum(data[i:min(len(data), i+nblock)]))

def update(ind, val):
    prev, data[ind] = data[ind], val
    decomposition[ind//nblock] += (val - prev)

def get_sum(l, r):
    lsqrt = l // nblock
    rsqrt = r // nblock

    if lsqrt >= rsqrt:
        return sum(data[l:r])
    return sum(data[l:(lsqrt + 1)*nblock]) + sum(decomposition[lsqrt+1:rsqrt]) + sum(data[rsqrt*nblock:r])

for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        update(b, c)
    else:
        print(get_sum(b, c))







