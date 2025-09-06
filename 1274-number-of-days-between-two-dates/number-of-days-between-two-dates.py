class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        monthDays = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365, 0]
        def isLeap(y):
            return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
        def toDays(date):
            y, m, d = map(lambda s: int(s), date.split("-"))
            days = (y-1) * 365
            # leap years
            days += (y-1) // 4
            days -= (y-1) // 100
            days += (y-1) // 400
            # month (and leap month)
            days += monthDays[m-2] + int(m > 2 and isLeap(y))
            # days
            days += d
            return days
        return abs(toDays(date1) - toDays(date2))
