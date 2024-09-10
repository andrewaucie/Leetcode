# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x,y):
            minNum = min(x,y)
            maxNum = max(x,y)
            if maxNum % minNum == 0:
                return minNum
            maxGCD = 1
            for i in range(minNum // 2 + 1 , 1, -1):
                if minNum % i == 0 and maxNum % i == 0:
                    return i
            return 1
        if not head or not head.next:
            return head
        temp = head
        while temp.next:
            maxGCD = gcd(temp.val, temp.next.val)
            tempNext = ListNode(val=maxGCD, next=temp.next)
            temp.next = tempNext
            temp = tempNext.next
        return head

                
            