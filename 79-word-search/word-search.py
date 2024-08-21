class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, x, y, visited):
            if (x,y) in visited:
                return False
            visited.add((x,y))

            if i == len(word)-1:
                return True

            a,b,c,d = False,False,False,False

            if x > 0 and board[x-1][y] == word[i+1]:
                a = dfs(i+1, x-1, y, visited)
            if y > 0 and board[x][y-1] == word[i+1]:
                b = dfs(i+1, x, y-1, visited)
            if x < len(board)-1 and board[x+1][y] == word[i+1]:
                c = dfs(i+1, x+1, y, visited)
            if y < len(board[0])-1 and board[x][y+1] == word[i+1]:
                d = dfs(i+1, x, y+1, visited)
            
            visited.remove((x,y))
            return a or b or c or d

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(0, i, j, set()):
                        return True
        return False
        
