"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = set()
        nodeDict = {}

        def dfs(node):
            if not node or node.val in visited:
                return

            visited.add(node.val)

            nodeDict[node.val] = Node(node.val)

            for neighbor in node.neighbors:
                dfs(neighbor)
                nodeDict[node.val].neighbors.append(nodeDict[neighbor.val])

        dfs(node)

        return nodeDict[1]