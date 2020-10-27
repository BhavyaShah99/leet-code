# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        curr = head
        while curr != None:
            l.append(curr.val)
            curr = curr.next
        n = len(l) - 1
        i = 0
        while i < len(l):
            if l[i] != l[n]:
                return False
            i += 1
            n -= 1
        return True