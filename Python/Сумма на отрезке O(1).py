s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
helper = [0] * len(s)
helper[0] = s[0]

for i in range(1, len(s)):
    helper[i] = helper[i-] + s[i]

# 4 - 6 сумма
print(helper)
print(helper[6] - helper[4])