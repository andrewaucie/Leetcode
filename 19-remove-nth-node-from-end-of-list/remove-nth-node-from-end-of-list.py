# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        nodeMap = {}
        node = head
        index = 0
        while node:
            nodeMap[index] = node
            node = node.next
            index += 1
        if len(nodeMap) - n == 0:
            temp = head
            head = head.next
            temp = None
        else:
            prev = nodeMap[len(nodeMap) - n - 1]
            remove = nodeMap[len(nodeMap) - n]
            prev.next = remove.next
            remove = None
        return head