# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        binary = []
        while head.next != None:
            binary.append(head.val)
            head = head.next
        binary.append(head.val)
        n = len(binary)-1
        num = 0
        for i in binary:
            num += (i * (2**n))
            n -= 1
        return num