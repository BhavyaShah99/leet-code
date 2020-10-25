# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root):
        if root == None:
            return
        out = []
        if root.left != None:
            out += self.inorderTraversal(root.left)
        out.append(root.val)
        if root.right != None:
            out += self.inorderTraversal(root.right)
        return out
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree1 = self.inorderTraversal(root1)
        tree2 = self.inorderTraversal(root2)
        new = []
        if tree1:
            new += tree1
        if tree2:
            new += tree2
        new.sort()
        return new