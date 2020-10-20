# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        out = []
        if root.left != None:
            out += self.postorderTraversal(root.left)
        if root.right != None:
            out += self.postorderTraversal(root.right)
        out.append(root.val)
        return out