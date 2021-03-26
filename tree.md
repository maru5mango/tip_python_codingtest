class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1
    def depth(self):
        leftDepth = self.left.depth() if self.left else 0
        rightDepth = self.right.depth() if self.right else 0
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1

class BinaryTree:
    def __init__(self, r):
        self.root = r
