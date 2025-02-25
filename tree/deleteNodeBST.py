# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def find_min(r):
            while r.left:
                r = r.left
            return r

        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # it has two children , find min of right subtree
            successor = find_min(root.right)
            root.val = successor.val  # Copy successor's value to root
            root.right = self.deleteNode(root.right, successor.val)
        return root





