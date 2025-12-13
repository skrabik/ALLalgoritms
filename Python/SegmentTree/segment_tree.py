# habr: https://habr.com/ru/articles/808511/

def next_power_of_two(n):
    """Находит ближайшую степень двойки, не меньшую чем n"""
    if n <= 0:
        return 1
    return 1 << (n - 1).bit_length()

class SegmentTree:
    def __init__(self, array):
        n = next_power_of_two(len(array))*2
        self.tree = [0 for _ in range(n)]
        for i in range((n // 2) - 1, (n // 2) - 1 + len(array)):
            self.tree[i] = array[i - ((n // 2) - 1)]
        for i in range((n // 2) - 2, -1, -1):
            self.tree[i] = self.tree[i*2 + 1] + self.tree[i*2 + 2]

    def getSum(self, l, r):
        if l == r: return self.tree[l + (len(self.tree) // 2) - 1]
        l += (len(self.tree) // 2) - 1
        r += (len(self.tree) // 2) - 1
        res = 0
        while l <= r:
            if l % 2 == 0:
                res += self.tree[l]
            l = l // 2
            if r % 2 == 1:
                res += self.tree[r]
            r = (r // 2) - 1
        return res
        
    def update(self, index, value): # индексация при обновлении будет 0
        x = index + (len(self.tree) // 2) - 1
        self.tree[x] = value
        while x != 0:
            x = (x - 1) // 2
            self.tree[x] = self.tree[x*2 + 1] + self.tree[x*2 + 2]
        return True