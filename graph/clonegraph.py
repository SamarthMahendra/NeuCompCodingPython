"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional, List

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = dict()

        def clone(node):
            if not node:
                return None
            if node in visited:
                return visited[node]

            new = Node(node.val)
            visited[node] = new

            for n in node.neighbors:
                new.neighbors.append(clone(n))
            return new
        return clone(node)