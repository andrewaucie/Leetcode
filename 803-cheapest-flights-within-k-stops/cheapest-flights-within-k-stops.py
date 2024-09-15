class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        for fromCity, toCity, price in flights:
            graph[fromCity].add((toCity, price))
        # (city, totalPrice, stops)
        queue = [(0, src, 0)]
        visited = set()
        while queue:
            totalPrice, city, stops = heapq.heappop(queue)
            if city == dst:
                return totalPrice
            for toCity, price in graph[city]:
                if ((stops == k and toCity == dst) or stops < k) and (city, toCity, stops) not in visited:
                    visited.add((city, toCity, stops))
                    heapq.heappush(queue, (totalPrice + price, toCity, stops+1))
        return -1