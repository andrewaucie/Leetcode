class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        minRegular = 0
        minExpress = expressCost
        res = []

        for i in range(len(regular)):
            minRegular = min(minRegular + regular[i], minExpress + express[i])
            minExpress = min(minRegular + expressCost, minExpress + express[i])
            res.append(min(minRegular, minExpress))
        
        return res