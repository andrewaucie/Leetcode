class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # Monotonic stack, store indices
        # Once item is popped, return index difference
        stack = [0]
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                lastIndex = stack.pop()
                res[lastIndex] = i - lastIndex
            stack.append(i)
        return res


