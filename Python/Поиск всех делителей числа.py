import math

def all_del(num):
    answer = set()

    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            answer.add(i)
            answer.add(num // i)
    return answer

