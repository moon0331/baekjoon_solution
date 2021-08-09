# 트리 순회
import string
import sys

class Node:
    NODE_NAME = string.ascii_uppercase
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = left
        self.is_leaf = not any((self.left, self.right))

    def append_node(self, child_node, direction):
        if child_node == '.':
            return
        if direction == 'left':
            self.left = child_node
        elif direction == 'right':
            self.right = child_node
        self.is_leaf = True

    def __str__(self):
        return '{} : is_leaf = {}, left = {}, right = {}'.format(self.name, self.is_leaf)

def preorder(node):
    if not node:
        return
    print(node.name, end='')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.name, end='')
    inorder(node.right)

def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.name, end='')

N = int(input())

node_dict = {Node.NODE_NAME[i] : Node(Node.NODE_NAME[i]) for i in range(N)}
node_dict['.'] = '.'

for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    left_node, right_node = node_dict[left], node_dict[right]
    node_dict[node].append_node(left_node, 'left')
    node_dict[node].append_node(right_node, 'right')

for traversal in (preorder, inorder, postorder):
    traversal(node_dict['A'])
    print()
