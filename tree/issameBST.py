# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.left and root.left.val > root.val:
            return False
        if root.right and root.val > root.right.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
