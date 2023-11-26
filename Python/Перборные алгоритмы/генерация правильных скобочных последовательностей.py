m = int(input())
length = m

def true_queele2(data):
    open = {'(', '['}
    stack = []
    for i in range(len(data)):
        if data[i] in open:
            stack.append(data[i])
        else:
            if len(stack) == 0:
                return False
            elif data[i] == ')' and stack[-1] == '[':
                return False
            elif data[i] == ']' and stack[-1] == '(':
                return False
            else:
                stack.pop(-1)
    return True

def generate_permutations(n, m=2, prefix=None, c_open=0, c_close=0):
    if c_open > length // 2:
        return
    # if c_close > length // 2:
    #     return
    prefix = prefix or []
    if m == 0:
        print(''.join(prefix))
        return
    for digit in n:
        prefix.append(digit)
        if digit == '(' or digit == '[':
            c_open += 1
        if digit == ']' or digit == ')':
            c_close += 1
        if true_queele2(prefix) == False:
            if digit == ']' or digit == ')':
                c_close -= 1
            prefix.pop()
            continue
        generate_permutations(n, m-1, prefix, c_open, c_close)
        if digit == '(' or digit == '[':
            c_open -= 1
        if digit == ']' or digit == ')':
            c_close -= 14

        prefix.pop()

import  datetime
start = datetime.datetime.now()
generate_permutations(n=['(', '[', ']', ')'], m=m)
stop = datetime.datetime.now()
print(stop - start)