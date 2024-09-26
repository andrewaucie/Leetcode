class MyCalendar:

    def __init__(self):
        self.d = {}
        self.count = 0
        
    '''
    O(nlogN) sorting
    outer loop * remove => O(N) * O(N) => O(N^2)
    '''
    
    def checkOverlaps(self, newKey):
        bookings = list(self.d.values())
        lst = []
        for start, end in bookings:
            lst.append((start, +1)) # one booking added at startingtime = start
            lst.append((end, -1)) # booking ends at timestamp = end
            
        lst.sort()
        overlaps = 0
        for book in lst:
            overlaps += book[1]
            if overlaps > 1:
                del self.d[newKey] # remove the booking that is causing problems (triple overlap)
                return False
        return True
    
    
    def book(self, start: int, end: int) -> bool:
        self.count += 1
        self.d[self.count] = (start,end)
        return self.checkOverlaps(self.count)