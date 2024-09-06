# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        node = head
        dummy = ListNode(next=head)
        prev = dummy
        while node:
            if node.val in nums:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        head = dummy.next
        return head