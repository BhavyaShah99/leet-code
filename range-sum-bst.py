# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        s = self.getNodes(root)
        summ = 0
        for i in s:
            if i >= L and i <= R:
                summ+=i
        return summ
            
    def getNodes(self, root):
        if root == None:
            return
        s = []
        if root.left != None:
            s += self.getNodes(root.left)
        s.append(root.val)
        if root.right != None:
            s += self.getNodes(root.right)
        return s