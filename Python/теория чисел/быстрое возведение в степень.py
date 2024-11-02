def speed(a, b):
    res = a
    while b > 1:
        print(res, b)
        if b & 1 == 1:
            res *= a 
            b -= 1
        else:
            res **= 2
            b //= 2
    return res

print(speed(2, 5))

# for i in range(1, 101):
#     for j in range(1, 101):
#         if speed(i, j) != i**j:
#             print(i, j)
#             break 
# print("end")
