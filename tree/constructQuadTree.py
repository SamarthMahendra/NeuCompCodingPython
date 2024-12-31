"""
# Definition for a QuadTree node.

"""

from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def check_all_same(g):
            ref = g[0][0]
            for i in range(len(g)):
                for j in range(len(g[0])):
                    if g[i][j] != ref:
                        return False
            return True

        def make_tree(grid):
            if not grid:
                return None
            if check_all_same(grid):
                return Node(grid[0][0] == 1, True, None, None, None, None)
            n = len(grid)
            mid = n // 2

            topLeft = make_tree([row[:mid] for row in grid[:mid]])
            topRight = make_tree([row[mid:] for row in grid[:mid]])
            bottomLeft = make_tree([row[:mid] for row in grid[mid:]])
            bottomRight = make_tree([row[mid:] for row in grid[mid:]])

            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        return make_tree(grid)





