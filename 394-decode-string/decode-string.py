class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        memo = {}
        def backtrack(string):
            curr = ""
            num = ""
            i = 0
            while i < len(string):
                if string[i].isalpha():
                    curr += string[i]
                elif string[i].isnumeric():
                    num += string[i]
                elif string[i] == "[":
                    curr += int(num) * backtrack(string[i+1:])
                    break
                elif string[i] == "]":
                    return curr
                i += 1
            brackets = 0
            while i < len(string):
                if string[i] == "[":
                    brackets += 1
                elif string[i] == "]":
                    brackets -= 1
                i += 1
                if brackets == 0:
                    break
            if i == len(string):
                return curr
            curr += backtrack(string[i:])
            return curr
        return backtrack(s)

