class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # [11, 6], n=6
        # product = max(2,3,3,3,3)
        left = 1
        right = max(quantities)
        minX = right
        # binary search to find the minimum x
        while left < right:
            mid = (left + right) // 2
            stores = 0
            #maxProduct = float('-inf')
            for q in quantities:
                #maxProduct = max(maxProduct, )
                stores += int(math.ceil(q / mid))
            # if stores == n:
            #     minX = (minX, maxProduct)
            if stores > n:
                left = mid + 1
            else:
                right = mid
        return left

