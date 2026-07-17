# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = slow.next = None
        while curr:
            nnext = curr.next
            curr.next = prev
            prev = curr
            curr = nnext
        
        left = head
        right = prev

        while right:
            lnext = left.next
            rnext = right.next

            left.next = right
            right.next = lnext
            
            left = lnext
            right = rnext
