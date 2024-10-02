class DSU_New:
    def __init__(self, n):
        self.sets = [i for i in range(n+1)]
        self.quantity = [1 for i in range(n+1)]
    
    def get_parent(self, u):
        if self.sets[u] == u:
            return u
        self.sets[u] = self.get_parent(self.sets[u])
        return self.sets[u]
 
    def union(self, u, v):
        u = self.get_parent(u)
        v = self.get_parent(v)
        if u == v: 
            return
        if self.quantity[u] < self.quantity[v]:
            u, v = v, u
        self.quantity[u] += self.quantity[v]
        self.sets[v] = u
 
    def check(self, u, v):
        return self.get_parent(u) == self.get_parent(v)
        
    def print_one(self, u, v):
        if (self.check(u, v)):
            return 'YES'
        else:
            return 'NO'
    
n, m, k = map(int, input().split())
 
tree = DSU_New(n)
 
for _ in range(m):
    input()
 
stack = list()
for _ in range(k):
    stack.append(input().split())
answer = list()
 
for i in range(len(stack)-1, -1, -1):
    type, u, v = stack[i][0], int(stack[i][1]), int(stack[i][2])
 
    if type == 'ask':
        answer.append(tree.print_one(u, v))
    else: 
        tree.union(u, v)

for i in range(len(answer)-1, -1, -1):
    print(answer[i])