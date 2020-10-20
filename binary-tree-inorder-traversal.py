# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        out = []
        if root.left != None:
            out += self.inorderTraversal(root.left)
        out.append(root.val)
        if root.right != None:
            out += self.inorderTraversal(root.right)
        return out
        