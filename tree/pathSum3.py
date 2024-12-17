Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict

        rs = defaultdict(int)
        rs[0] = 1

        def res(node=root, sm=0):
            if not node:
                return 0
            currSum = sm + node.val
            cnt = rs[currSum - targetSum]
            rs[currSum] += 1
            cnt += res(node.left, currSum) + res(node.right, currSum)
            rs[currSum] -= 1
            return cnt

        return res()

