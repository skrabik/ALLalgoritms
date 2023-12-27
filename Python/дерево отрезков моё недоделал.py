class tree_of_segments:
    def __init__(self, data, f):
        self.n = len(data)
        data = [0 for i in range(self.n)] + data
        for i in reversed(range(self.n)):
            data[i] = f(data[2*i], data[2*i+1])
        self.data = data
    # def get_val(self, l, r):
    #     rez = 0
    #     i = 0
    #     while True:

def f(a, b):
    return a + b

A = [1, 2, 3, 4]
tree = tree_of_segments(A, f=f)
print(tree.data)




