n, target = map(int, input().split())

def f(n):
    k = 1 # однозначные числа
    x = 0 # количество цифр до начала нужных чисел в разряде
    i = 1
    while x < n:
        x += 9*i*(10**(i-1))
        if x < n:
            k += 9*i*(10**(i-1))
            i += 1
    # k - позиция первой цифры i значного числа
    # i - стольки значное число нам надо

    # надо найти это число

    num_count = (n - k) // i # количетво чисел между первым и нужным
    start = k + num_count*i # позиция начала числа
    s = 10**(i-1) + num_count # число
    razn = i + start - n
    for j in range(0, razn):
        res = s % 10
        s = s // 10
    return res, i, num_count # веернёт цифру на позиции n, сколько значное число и количство стольки же значных чисел перед ним

import math
if f(n)[0] == target:
    print(0)
else:
    k = 0
    while f(n)[0] != target:
        n += 1
        k += 1
    s, i, num_count = f(n)
    if k <= num_count*i:
        print(math.ceil(k/i))
    else:
        res = num_count
        k -= num_count*i
        res += math.ceil(k/(i-1))
        print(res)