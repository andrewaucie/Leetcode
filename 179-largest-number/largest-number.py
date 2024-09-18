class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        stringNums = [str(x) for x in nums]
        stringNums.sort(key=lambda x: x*10, reverse=True)
        if stringNums[0] == "0":
            return "0"
        return ''.join(stringNums)
