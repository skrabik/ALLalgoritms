

class CommonTree:

    class Node:
        def __init__(self, value=None):
            self.val = value

    def __init__(self):
        self.node_list = []
        self.tree = []

    node_list = []
    tree = []

    def add_v(self, value):
        self.node_list.append(self.Node(value))
        self.tree.append([])

    def add_e(self, v1, v2):
        self.tree[v1].append(v2)
        self.tree[v2].append(v1)






a = CommonTree()