class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        string = "0"
        for _ in range(n-1):
            string += "1"
            for i in range(len(string)-2, -1, -1):
                string += str(int(string[i]) ^ 1)
        print(string)
        return string[k-1]