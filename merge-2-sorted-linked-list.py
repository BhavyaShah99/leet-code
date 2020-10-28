# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        merged = None
        other = None
        if l1.val <= l2.val:
            merged = l1
            other = l2
        else:
            merged = l2
            other = l1
        curr = merged
        while curr != None:
            if other == None:
                break
            if curr.next == None:
                curr.next = other
                break
            if(curr.val <= other.val and other.val <= curr.next.val):
                temp = curr.next
                curr.next = other
                temp2 = other.next
                other.next = temp
                other = temp2
                curr = curr.next
            else:
                curr = curr.next
        return merged