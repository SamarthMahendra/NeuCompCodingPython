# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedHelper(self, root):
        if not root:
            return True, 0

        left_balanced, left_height = self.isBalancedHelper(root.left)
        right_balanced, right_height = self.isBalancedHelper(root.right)
        is_balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
        )

        height = 1 + max(left_height, right_height)

        return is_balanced, height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root)[0]
