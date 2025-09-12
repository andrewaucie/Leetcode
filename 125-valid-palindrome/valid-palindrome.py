class Solution:
    def isPalindrome(self, s: str) -> bool:
        # "A man, a plan, a canal: Panama"
        # Initial Bruteforce:
        forward = ""
        backward = ""
        for l in s:
            if l.isalnum():
                forward += l.lower()
        for l in reversed(s):
            if l.isalnum():
                backward += l.lower()
        return forward == backward