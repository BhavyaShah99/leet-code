# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        listset = {ListNode(None)}
        while head:
            if head not in listset:
                listset.add(head)
            else:
                return True
            head = head.next
        return False