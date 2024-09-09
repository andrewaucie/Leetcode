class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p, s in zip(position, speed)]
        cars.sort(key=lambda x:x[0], reverse=True)
        fleets = []
        for p,s in cars:
            timeToTarget = (target - p) / s
            fleets.append(timeToTarget)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)