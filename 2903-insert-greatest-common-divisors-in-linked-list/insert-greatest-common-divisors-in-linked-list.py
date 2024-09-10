# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        if not head or not head.next:
            return head
        temp = head
        while temp.next:
            maxGCD = gcd(temp.val, temp.next.val)
            tempNext = ListNode(val=maxGCD, next=temp.next)
            temp.next = tempNext
            temp = tempNext.next
        return head

                
            