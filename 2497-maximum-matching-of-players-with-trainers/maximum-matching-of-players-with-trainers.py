class Solution:
    def matchPlayersAndTrainers(self, players:  List[int], 
                                      trainers: List[int]) -> int:
        ans = 0
        trainers.sort()
        heapify(players)

        for t in trainers:

            if players and players[0] <= t:
                heappop(players)

                ans+= 1

        return ans