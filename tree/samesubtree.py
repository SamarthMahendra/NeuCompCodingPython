# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def issame(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and issame(a.right, b.right) and issame(a.left, b.left)

        def dfs(root):
            if not root:
                return False

            if issame(root, subRoot):
                return True
            else:
                return dfs(root.left) or dfs(root.right)

        return dfs(root)
