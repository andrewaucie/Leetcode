# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        result = PolyNode()
        temp = result
        while poly1 or poly2:
            if poly1 and (not poly2 or poly1.power > poly2.power):
                temp.next = PolyNode(x=poly1.coefficient, y=poly1.power)
                temp = temp.next
                poly1 = poly1.next
            elif poly2 and (not poly1 or poly2.power > poly1.power):
                temp.next = PolyNode(x=poly2.coefficient, y=poly2.power)
                temp = temp.next
                poly2 = poly2.next
            elif poly1 and poly2 and poly1.power == poly2.power:
                coefficient = poly1.coefficient + poly2.coefficient
                if coefficient != 0:
                    temp.next = PolyNode(x=coefficient, y=poly1.power)
                    temp = temp.next
                poly1 = poly1.next
                poly2 = poly2.next
        return result.next
        