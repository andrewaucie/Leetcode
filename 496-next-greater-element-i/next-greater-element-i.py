class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexMap = {nums2[i] : i for i in range(len(nums2))}
        res = []
        for n in nums1:
            greater = -1
            for i in range(indexMap[n]+1, len(nums2)):
                if nums2[i] > n:
                    greater = nums2[i]
                    break
            res.append(greater)
        return res
            