# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        temp = dummy
        while l1 or l2:
            digit = carry
            if l1:
                digit += l1.val
                l1 = l1.next
            if l2:
                digit += l2.val
                l2 = l2.next
            temp.next = ListNode(val=(digit % 10))
            temp = temp.next
            carry = digit // 10
        if carry != 0:
            temp.next = ListNode(val=carry)
        return dummy.next

