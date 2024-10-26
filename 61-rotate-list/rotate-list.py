# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        size = 0
        temp = head
        while True:
            size += 1
            if not temp.next:
                temp.next = head
                break
            temp = temp.next
        k %= size
        temp = head
        for _ in range(size-k-1):
            temp = temp.next
        newHead = temp.next
        temp.next = None
        return newHead
