class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # [4,1,2]
        # [1,3,4,2]

        # [1,3]
        # [3]
        # monotonic stack of nums2
        # for n in nums2:
        #     while n > stack[-1]:
        #          
        #     stack.append(n)
        indexMap = {nums1[i] : i for i in range(len(nums1))}
        res = [-1] * len(nums1)
        stack = []
        for n in nums2:
            while stack and n > stack[-1]:
                poppedNum = stack.pop()
                if poppedNum in indexMap:
                    res[indexMap[poppedNum]] = n
            stack.append(n)
        return res