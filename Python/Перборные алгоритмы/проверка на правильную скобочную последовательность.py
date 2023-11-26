data = input()
data = [i for i in data]

def true_queele(data):
    open ={'(', '['}
    stack = []
    for i in range(len(data)):
        if data[i] in open:
            stack.append(data[i])
        else:
            if len(stack) == 0:
                return False
            elif data[i] == '}' and (stack[-1] == '(' or stack[-1] == '['):
                return False
            elif data[i] == ')' and (stack[-1] == '{' or stack[-1] == '['):
                return False
            elif data[i] == ']' and (stack[-1] == '(' or stack[-1] == '{'):
                return False
            else:
                stack.pop(-1)
    if len(stack) == 0:
        return True
    else:
        return False

print(true_queele(data))