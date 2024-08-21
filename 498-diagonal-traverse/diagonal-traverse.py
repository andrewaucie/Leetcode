class Solution:
  def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    # Step 1
    result = []
    # Step 2
    m, n = len(mat), len(mat[0])
    i = j = direction = 0
    
    # Step 3
    for _ in range(m * n):
        result.append(mat[i][j])
        
        if direction == 0: # Up-right direction
            if j == n - 1:
                direction = 1 # Change direction to down-left
                i += 1
            elif i == 0:
                direction = 1 # Change direction to down-left
                j += 1
            else:
                i -= 1
                j += 1
        else: # Down-left direction
            if i == m - 1:
                direction = 0 # Change direction to up-right
                j += 1
            elif j == 0:
                direction = 0 # Change direction to up-right
                i += 1
            else:
                i += 1
                j -= 1
    
    # Step 4
    return result