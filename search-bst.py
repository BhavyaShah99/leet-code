# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr = root
        find = None
        while curr != None:
            if curr.val == val:
                find = curr
                curr = None
            else:
                if val < curr.val:
                    curr = curr.left
                else:
                    curr = curr.right
        if find != None:
            return find
        return None