class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        indexMap = {row[i] : i for i in range(len(row))}
        res = 0
        for i in range(0, len(row), 2):
            firstPerson = row[i]

            if firstPerson % 2 == 0:
                partner = firstPerson + 1
            else:
                partner = firstPerson - 1

            nextPerson = row[i+1]
            if nextPerson != partner:
                partnerIndex = indexMap[partner]
                row[partnerIndex] = nextPerson
                indexMap[nextPerson] = partnerIndex
                res += 1
        return res
