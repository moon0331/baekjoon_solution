import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.child = []

N = int(sys.stdin.readline())

node_dict = {i:Node(i) for i in range(1, N+1)}

