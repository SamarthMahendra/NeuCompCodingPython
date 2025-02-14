# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque([root])

        res = []
        level_res = []
        while queue:
            level = []
            nodes_in_level = len(queue)
            for i in range(nodes_in_level):
                cur = queue.popleft()
                if cur:
                    level.append(cur.val)
                    if i == nodes_in_level - 1:
                        res.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
            level_res.append(level)

        return res





