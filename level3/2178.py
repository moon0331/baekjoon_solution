import sys
from collections import Queue

def BFS(maze, visited):
    visited[0][0] = 1
    q = Queue()