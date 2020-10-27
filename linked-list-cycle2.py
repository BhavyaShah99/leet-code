# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        curr = head
        tracker = {curr}
        while curr != None:
            if curr.next not in tracker:
                tracker.add(curr.next)
            else:
                return curr.next
            curr = curr.next
        return None