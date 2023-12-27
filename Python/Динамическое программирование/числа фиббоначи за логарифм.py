def matrix_multiplication(M1, M2):
    M3 = [[0 for i in range(len(M2[0]))] for i in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            M3[i][j] = sum([M1[i][k]*M2[k][j] for k in range(len(M2))])
    return M3

def exponentiation(M, k):
    if k == 2:
        return matrix_multiplication(M, M)
    if k % 2 == 0:
        return exponentiation(exponentiation(M, k//2), 2)
    else:
        return matrix_multiplication(M, exponentiation(M, k-1))


def get_n_num_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    FIB_MATR = [[1, 1],
                [1, 0]]

    return matrix_multiplication(exponentiation(FIB_MATR, n-1), [[1, 1]])[0][0]

print(get_n_num_fib(10000))
