# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for curr in lists:
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next
        head = ListNode()
        temp = head
        while heap:
            temp.next = ListNode(val=heapq.heappop(heap))
            temp = temp.next
        return head.next