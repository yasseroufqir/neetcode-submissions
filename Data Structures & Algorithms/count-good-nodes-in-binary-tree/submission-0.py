# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,Val):
            if not node:
                return 0
            res = 1 if node.val >= Val else 0
            Val = max(Val,node.val)
            res+= dfs(node.right,Val)
            res+= dfs(node.left,Val)
            return res
        return dfs(root,root.val)