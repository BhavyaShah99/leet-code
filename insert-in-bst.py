class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        newNode = TreeNode(val)
        if root == None:
            return newNode
        curr = root
        par = None
        while curr != None:
            par = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if val < par.val:
            par.left = newNode
        else:
            par.right = newNode
        return root