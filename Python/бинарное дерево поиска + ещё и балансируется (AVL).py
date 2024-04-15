"""
Helper functions to support AVL re-balancing.

These depend on having a binary tree structure with a
compute_height() method to maintain height information.
"""

def rotate_right(node):
    """Perform right rotation around given node."""
    new_root = node.left
    grandson = new_root.right
    node.left = grandson
    new_root.right = node

    node.compute_height()
    return new_root

def rotate_left(node):
    """Perform left rotation around given node."""
    new_root = node.right
    grandson = new_root.left
    node.right = grandson
    new_root.left = node

    node.compute_height()
    return new_root

def rotate_left_right(node):
    """Perform left, then right rotation around given node."""
    child = node.left
    new_root = child.right
    grand1  = new_root.left
    grand2  = new_root.right
    child.right = grand1
    node.left = grand2

    new_root.left = child
    new_root.right = node

    child.compute_height()
    node.compute_height()
    return new_root

def rotate_right_left(node):
    """Perform right, then left rotation around given node."""
    child = node.right
    new_root = child.left
    grand1  = new_root.left
    grand2  = new_root.right
    child.left = grand2
    node.right = grand1

    new_root.left = node
    new_root.right = child

    child.compute_height()
    node.compute_height()
    return new_root

def resolve_left_leaning(node):
    """If node is right-leaning, rebalance and return new root node for subtree."""
    if node.height_difference() == 2:
        if node.left.height_difference() >= 0:
            node = rotate_right(node)
        else:
            node = rotate_left_right(node)
    return node

def resolve_right_leaning(node):
    """If node is right-leaning, rebalance and return new root node for subtree."""
    if node.height_difference() == -2:
        if node.right.height_difference() <= 0:
            node = rotate_left(node)
        else:
            node = rotate_right_left(node)
    return node

def check_avl_property(n):
    """
    Validates that the height for each node in the tree rooted at 'n' is correct, and that
    the AVL property regarding height difference is correct. This is a helpful debugging tool.
    """
    if n is None:
        return -1

    left_height = check_avl_property(n.left)
    right_height = check_avl_property(n.right)

    if n.height != 1 + max(left_height, right_height):
        raise ValueError('AVL height incorrect at {}'.format(n.value))

    if left_height - right_height < -1 or left_height - right_height > 1:
        raise ValueError('AVL tree property invalidated at {}'.format(n.value))

    return n.height

class BinaryNode:
    """
    Node structure to use in a binary tree.

    Attributes
    ----------
        left   - left child (or None)
        right  - right child (or None)
        value  - value stored by Node
        height - computed height of node in AVL tree
    """
    def __init__(self, val):
        self.value = val
        self.left  = None
        self.right = None
        self.height = 0

    def height_difference(self):
        """
        Compute height difference of node's children in BST. Can return
        a negative number or positive number.
        """
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        return left_height - right_height

    def compute_height(self):
        """Compute height of node in BST."""
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = 1 + max(left_height, right_height)

    def size(self):
        """Return number of nodes in subtree rooted at node."""
        ct = 1
        if self.left:  ct += self.left.size()
        if self.right: ct += self.right.size()
        return ct

class BinaryTree:
    """
    A Binary tree contains the root node, and methods to manipulate the tree.
    """
    def __init__(self):
        self.root = None

    def is_empty(self):
        """Returns whether tree is empty."""
        return self.root is None

    def insert(self, val):
        """Insert value into Binary Tree."""
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        """Inserts a new BinaryNode to the tree containing this value."""
        if node is None:
            return BinaryNode(val)

        if val <= node.value:
            node.left = self._insert(node.left, val)
            node = resolve_left_leaning(node)
        else:
            node.right = self._insert(node.right, val)
            node = resolve_right_leaning(node)

        node.compute_height()
        return node

    def min(self):
        """Return minimum value in tree without causing any changes."""
        if self.root is None:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.value

    def _remove_min(self, node):
        """
        Delete minimum value from subtree rooted at node.
        Have to make sure to compute_height on all affected ancestral nodes.
        """
        if node.left is None:
            return node.right

        # Might have made right-leaning, since deleted from left. Deal with it
        node.left = self._remove_min(node.left)
        node = resolve_right_leaning(node)
        node.compute_height()
        return node

    def remove(self, val):
        """Remove value from tree."""
        self.root = self._remove(self.root, val)

    def _remove(self, node, val):
        """Remove val from subtree rooted at node and return resulting subtree."""
        if node is None:
            return None

        if val < node.value:
            node.left = self._remove(node.left, val)
            node = resolve_right_leaning(node)
        elif val > node.value:
            node.right = self._remove(node.right, val)
            node = resolve_left_leaning(node)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # replace self value with node containing smallest value from right subtree
            original = node

            # find SMALLEST child in right subtree and remove it
            node = node.right
            while node.left:
                node = node.left

            node.right = self._remove_min(original.right)
            node.left = original.left

            # Might have made left-leaning by shrinking right side
            node = resolve_left_leaning(node)

        node.compute_height()
        return node

    def __contains__(self, target):
        """Check whether BST contains target value."""
        node = self.root
        while node:
            if target == node.value:
                return True
            if target < node.value:
                node = node.left
            else:
                node = node.right

        return False

    def __iter__(self):
        """In order traversal of elements in the tree."""
        for v in self._inorder(self.root):
            yield v

    def _inorder(self, node):
        """Inorder traversal of tree."""
        if node is None:
            return

        for v in self._inorder(node.left):
            yield v

        yield node.value

        for v in self._inorder(node.right):
            yield v

tree = BinaryTree()
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(7)
tree.insert(6)
tree.insert(1)
tree.insert(5)
tree.insert(8)

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)
# tree.remove(3)
# # tree.remove(4)
# print(tree.root.value)


