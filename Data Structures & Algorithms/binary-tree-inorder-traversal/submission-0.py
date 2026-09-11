class Solution:
    def inorderTraversal(self, root):
        res = []#shared across the recursion

        def dfs(node):#in order dfs
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res