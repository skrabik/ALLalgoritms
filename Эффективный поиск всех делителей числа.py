def f(x):
    answer = []
    for i in range(1, x + 1):
        if x % i == 0:
            answer.append(i)
    return answer