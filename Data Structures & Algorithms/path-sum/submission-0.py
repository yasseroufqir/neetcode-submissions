# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,sum): #building a dfs traversal that computes the sum from a node
            if not node:
                return False
            sum += node.val
            if not node.right and not node.left: #detecting a leaf
               return sum == targetSum
            return dfs(node.right,sum) or dfs(node.left,sum)
        return dfs(root,0)
            