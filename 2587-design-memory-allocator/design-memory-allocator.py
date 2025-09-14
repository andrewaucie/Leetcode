class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.memory = [0] * self.n

    def allocate(self, size: int, mID: int) -> int:
        index = 0
        while index < self.n:
            it = index
            while it < self.n and self.memory[it] == 0:
                if it == index + size - 1:
                    for i in range(index, it+1):
                        self.memory[i] = mID
                    return index
                it += 1
            index = it + 1
        return -1
    
    def freeMemory(self, mID: int) -> int:
        count = 0
        for i in range(self.n):
            if self.memory[i] == mID:
                self.memory[i] = 0
                count += 1
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)