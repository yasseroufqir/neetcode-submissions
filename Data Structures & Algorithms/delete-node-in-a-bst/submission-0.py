# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        else:
            # case 1: no right child
            if not root.right:
                return root.left
            
            # case 2: no left child
            if not root.left:
                return root.right
            
            # case 3: two children
            min_node = self.minValue(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root

    def minValue(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr