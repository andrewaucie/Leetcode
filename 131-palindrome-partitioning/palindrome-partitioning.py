class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            left = 0
            right = len(s)-1
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        res = []
        
        def backtrack(index, substrings):
            if index == len(s):
                res.append(substrings)
                return
            curr = ""
            while index < len(s):
                curr += s[index]
                if isPalindrome(curr):
                    backtrack(index+1, substrings + [curr])
                index += 1
        backtrack(0, [])
        return res
            