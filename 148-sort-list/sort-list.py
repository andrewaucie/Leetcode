# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.getMid(head)
        rightPartition = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(rightPartition)
        return self.merge(left, right)

    def getMid(self, head):
        slow = head
        fast = head
        while fast:
            if not fast.next or not fast.next.next:
                return slow
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, L, R):
        if not L:
            return R
        if not R:
            return L
        head = ListNode()
        dummy = head
        while L or R:
            if not L or (R and R.val < L.val):
                head.next = R
                R = R.next
            else:
                head.next = L
                L = L.next
            head = head.next
        return dummy.next
