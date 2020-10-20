# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        while head != None:
            temp = ListNode(head.val)
            head = head.next
            temp.next = newHead
            newHead = temp
        return newHead