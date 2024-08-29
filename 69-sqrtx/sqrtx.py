class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left, right = 0, x // 2
        while left <= right:
            print(left,right)
            mid = (left + right) // 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                right = mid-1
            else:
                left = mid+1
        return right
# 2*2, 3*3, 4*4, 5*5, 6*6

