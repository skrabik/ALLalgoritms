data = [1, 32, 23, 12, 10, 43, -2, 12]

class SegmentTree:
    def __init__(self, array):
        self.tree = ([0] * len(data)) + data


        # получение левого родителя и ребёнка: 
        # left_child = left_pred*2 + 1 
        # left_pred = (left_child - 1) // 2

        # получение правого родителя и ребёнка: 
        # rigth_child = rigth_pred*2 + 2 
        # rigth_pred = (right_child - 2) // 2

        for index in range((len(self.tree) // 2) - 1, -1, -1):
            left_child_value = self.tree[(index*2) + 1]
            rigth_child_value = self.tree[(index*2) + 2]
            self.tree[index] = left_child_value + rigth_child_value


obj = SegmentTree(data)
print(obj.tree)