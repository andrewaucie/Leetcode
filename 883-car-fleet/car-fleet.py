class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [10,8,0,5,3]
        # [2,4,1,1,3]
        sortedCars = sorted(list(zip(position, speed)), reverse=True)
        fleets = 0
        # time to target = math.ceil((target - position) / speed)
        # if time > prevTime, add to fleet
        prevTime = -1
        for pos, sp in sortedCars:
            time = (target - pos) / sp
            if time > prevTime:
                fleets += 1
                prevTime = time
        return fleets