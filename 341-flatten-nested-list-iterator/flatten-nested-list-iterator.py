# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.index = 0
        self.list = [] 
        self.flatten(nestedList)
    
    def flatten(self, nestedList):
        for it in nestedList:
            if it.isInteger():
                self.list.append(it.getInteger())
            else:
                self.flatten(it.getList())
        
    def next(self) -> int:
        val = self.list[self.index]
        self.index += 1
        return val
    
    def hasNext(self) -> bool:
        return self.index < len(self.list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())