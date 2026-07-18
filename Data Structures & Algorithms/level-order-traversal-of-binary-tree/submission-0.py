# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque()
        queue.append([root, 0])

        while queue:
            curr, depth = queue.popleft()
            if not curr:
                continue
    
            if len(res) > depth:
                res[depth].append(curr.val)
            else:
                res.append([curr.val])

            queue.append([curr.left, depth + 1])
            queue.append([curr.right, depth + 1])

        return res