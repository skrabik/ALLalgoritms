# массив фенвика
class fenvik_tree:
    def __init__(self, array):
        self.original = array.copy()
        for i in range(1, len(array)):
            array[i] = array[i] + array[i-1]
        data = [0]*len(array)
        for i in range(len(data)):
            if (i & (i+1))-1 >= 0:
                data[i] = array[i] - array[(i & (i+1))-1]
            else:
                data[i] = array[i]
        self.data = data

    def sum_to_zero(self, ind):
        if ind == 0:
            return self.data[0]
        rez = 0
        while ind > 0:
            rez += self.data[ind]
            ind = (ind & (ind+1))-1
        return rez

    def get_sum(self, l, r):
        return self.sum_to_zero(r) - self.sum_to_zero(l-1)

    def update(self, ind, val):
        val = val - self.original[ind]
        while ind < len(self.data):
            self.data[ind] += val
            ind = (ind | (ind + 1))

B = [1, 2, 3, 4, 5, 6, 7, 8]
# print(sum(B))
g = fenvik_tree(B)
g.update(7, -3)
print(g.get_sum(0, 7))

# вроде работает, но удостоверься, Рома!
# https://www.youtube.com/watch?v=muW1tOyqUZ4&t=412s




