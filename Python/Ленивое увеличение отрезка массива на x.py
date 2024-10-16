a = [0 for _ in range(10)]

helper = [0 for i in range(len(a)+1)]

def push ():
    pref = 0
    for i in range(len(helper)-1):
        pref += helper[i]
        a[i] += pref
    for i in range(len(helper)):
        helper[i] = 0

def update(a, b):
    helper[a] += 1
    helper[b+1] -= 1

update(1, 2)
print(helper)
push()
print(a)