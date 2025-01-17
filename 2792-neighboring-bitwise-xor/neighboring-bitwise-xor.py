class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # [a,b,c]
        # [(a^b), (b^c), (c^a)]
        # (a^b)^(b^c)^(c^a)
        # a^(b^b)^(c^c)^a
        # a^0^a
        # a^a^0
        # 0^0
        # 0
        XORsum = 0
        for n in derived:
            XORsum ^= n
        return XORsum == 0