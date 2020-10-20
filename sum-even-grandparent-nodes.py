# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    summed = 0
    
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.search(root, None, None)
        return self.summed
        
    def search(self, node, par, gpar):
        if node == None:
            return
        if gpar != None and gpar.val%2==0:
            self.summed += node.val
        self.search(node.left, node, par)
        self.search(node.right, node, par)