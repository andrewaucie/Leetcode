# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]

        # 0 for Right, 1 Down, 2 Left, 3 Up
        d = 0
        dirMap = [(0,1), (1,0), (0, -1), (-1,0)]

        temp = head
        x,y = 0,0
        while temp:
            res[x][y] = temp.val
            temp = temp.next
            # Compute next position
            nextX, nextY = x + dirMap[d][0], y + dirMap[d][1]
            if not (0 <= nextX < m and 0 <= nextY < n and res[nextX][nextY] == -1):
                d = (d+1)%4
                nextX, nextY = x + dirMap[d][0], y + dirMap[d][1]
            x,y = nextX, nextY
        return res
