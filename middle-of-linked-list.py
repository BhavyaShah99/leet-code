# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        curr = head
        while curr!=None:
            length += 1
            curr = curr.next
        middle = 0
        if length%2==0:
            middle = length/2
        else:
            middle = length//2
        curr1 = head
        ct = 0
        while ct < middle:
            curr1 = curr1.next
            ct+=1
        return curr1