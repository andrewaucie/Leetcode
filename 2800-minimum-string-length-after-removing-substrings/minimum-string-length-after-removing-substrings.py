class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for letter in s:
            if not stack or stack[-1] + letter not in {"AB", "CD"}:
                stack.append(letter)
            else:
                stack.pop()
        return len(stack)