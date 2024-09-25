from math import floor, ceil
n = int(input())
k = int(input())

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

info = [i for i in range(1, n+1)]
while len(info):

    block = fact(len(info)-1)
    
    next_id = ceil(k / block)
    k = k % block
    print(info.pop(next_id-1), end=' ')
    