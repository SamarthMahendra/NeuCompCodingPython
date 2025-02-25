# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return

        root_val = preorder.pop(0)

        root_index = inorder.index(root_val)

        left_tree = self.buildTree(preorder, inorder[:root_index])
        right_tree = self.buildTree(preorder, inorder[root_index + 1:])
        return TreeNode(root_val, left_tree, right_tree)
