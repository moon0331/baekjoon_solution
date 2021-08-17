# binary search tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)