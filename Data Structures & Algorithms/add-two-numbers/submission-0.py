# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()

        curr = res
        num1 = l1
        num2 = l2
        carry = 0

        while num1 and num2:
            summ = num1.val + num2.val + carry
            carry = summ // 10
            curr.next = ListNode()
            curr = curr.next
            curr.val = summ % 10
            num1 = num1.next
            num2 = num2.next

        while num1:
            summ = num1.val + carry
            carry = summ // 10
            curr.next = ListNode()
            curr = curr.next
            curr.val = summ % 10
            num1 = num1.next

        while num2:
            summ = num2.val + carry
            carry = summ // 10
            curr.next = ListNode()
            curr = curr.next
            curr.val = summ % 10
            num2 = num2.next

        if carry:
            curr.next = ListNode()
            curr = curr.next
            curr.val = carry

        return res.next
