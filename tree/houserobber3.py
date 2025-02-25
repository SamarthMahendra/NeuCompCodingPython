# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(r):
            if not r:
                return (0, 0)

            left_robbed, left_not_robbed = dfs(r.left)
            right_robbed, right_not_robbed = dfs(r.right)

            rob_this = r.val + left_not_robbed + right_not_robbed

            skip_this = max(left_robbed, left_not_robbed) + max(right_robbed, right_not_robbed)

            return (rob_this, skip_this)

        return max(dfs(root))

