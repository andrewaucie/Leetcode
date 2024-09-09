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
        stuck = 0
        while temp:
            res[x][y] = temp.val
            nextX, nextY = x + dirMap[d][0], y + dirMap[d][1]
            if 0 <= nextX < m and 0 <= nextY < n and res[nextX][nextY] == -1:
                temp = temp.next
                x = nextX
                y = nextY
                stuck = 0
            else:
                d = (d+1)%4
                stuck += 1 
                if stuck == 4:
                    return res
        return res
