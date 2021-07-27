# DFS와 BFS

import sys
from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.connect = []

    def addChildNode(self, node):
        self.connect.append(node)
        node.connect.append(self)
        
def DFS(node):
    st = []
    visited = []
    st.append(node)
    while st:
        n = st.pop()
        if not n in visited:
            print(n.val, end=' ')
            visited.append(n)
            st.extend(sorted(n.connect, key = lambda x: x.val, reverse=True))
    print()

def BFS(node):
    q = deque()
    visited = []
    q.append(node)
    while q:
        n = q.popleft()
        if not n in visited:
            print(n.val, end =' ')
            visited.append(n)
            q.extend(n.connect)
    print()



N, M, V = map(int, sys.stdin.readline().split())

nodes = [Node(i) for i in range(N+1)] # 0은 dummy

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    nodes[x].addChildNode(nodes[y])

for node in nodes:
    node.connect.sort(key=lambda x : x.val)

DFS(nodes[V])
BFS(nodes[V])