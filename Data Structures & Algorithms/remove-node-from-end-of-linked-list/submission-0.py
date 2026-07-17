# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        for _ in range(n):
            curr = curr.next

        if curr == None:
            return head.next

        lagcurr = head
        prev = None
        while curr:
            prev = lagcurr
            lagcurr = lagcurr.next
            curr = curr.next
        prev.next = lagcurr.next
        return head
            
