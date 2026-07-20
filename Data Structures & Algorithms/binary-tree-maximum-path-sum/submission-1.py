# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(node):
            nonlocal res
            if not node:
                return None

            left_val = dfs(node.left) or 0
            right_val = dfs(node.right) or 0

            res = max(res, node.val + max(left_val, 0) + max(right_val, 0))

            return node.val + max(left_val, right_val, 0)

        dfs(root)

        return res