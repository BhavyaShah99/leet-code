# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        curr = head
        count = 0
        while curr != None:
            if curr.val in G and (curr.next == None or curr.next.val not in G):
                count += 1
            curr = curr.next
        return count