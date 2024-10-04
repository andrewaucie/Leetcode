class Solution:
    def expand(self, s: str) -> List[str]:
        
        res = []
        def dfs(i, curr):
            if i >= len(s):
                res.append(curr)
                return
            if s[i] == '{':
                endIndex = i
                for j in range(i+1, len(s)):
                    if s[j] == '}':
                        endIndex = j
                        break
                for j in range(i+1, endIndex):
                    if s[j] != ',':
                        dfs(endIndex+1, curr + s[j])
            elif s[i] != '}':
                dfs(i+1, curr + s[i])
        dfs(0, "")
        return sorted(res)

