def generate_permutations(n, m=-1, prefix = None):
    if m == -1:
        m = n
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep='')
        return
    for digit in range(1, n+1):
        if digit not in prefix:
            prefix.append(digit)
            generate_permutations(n, m-1, prefix)
            prefix.pop()

generate_permutations(n=3)
print()
s = [1, 2, 3]
def permutations(per, n):
    if n < 2:
        print(*per, sep='')
    else:
        for j in range(n-1, -1, -1):
            per[j], per[n-1] = per[n-1], per[j]
            permutations(s, n-1)
            per[j], per[n - 1] = per[n - 1], per[j]

permutations(s, len(s))