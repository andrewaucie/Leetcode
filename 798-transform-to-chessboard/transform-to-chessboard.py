import numpy as np
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        ans = 0
        rowCnt = Counter(map(tuple, board))
        colCnt = Counter(zip(*board))

        for count in (rowCnt, colCnt):
            # check if only two types of lines
            if len(count) != 2:
                return -1
            
            # check if count of diff of two types of lines is at most 1
            if sorted(count.values()) != [n//2, (n+1)//2]:
                return -1

            # check each type of line has count diff of 0 and 1 = at most 1
            for line in count:
                cnt = Counter(line)
                if sorted(count.values()) != [n//2, (n+1)//2]:
                    return -1
            
            # check if two lines are complementary
            line1, line2 = count
            if not all(x^y for x,y in zip(line1, line2)):
                return -1
            
            if n % 2:
                # if n is odd, first number is majority num
                expect = 1 if line1.count(1) > line1.count(0) else 0
                moves = 0
                for x in line1:
                    moves += x^expect
                    expect ^= 1

                ans += moves // 2
            else:
                moves = float('inf')
                for expect in (0,1):
                    curMoves = 0
                    for x in line1:
                        curMoves += x^expect
                        expect ^= 1
                    moves = min(moves, curMoves)
                ans += moves // 2
        return ans

