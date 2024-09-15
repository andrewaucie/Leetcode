class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Graph represented as adjacency list
        graph = defaultdict(list)
        for fromCity, toCity, price in flights:
            graph[fromCity].append((toCity, price))
        # Priority queue (min-heap) to store (totalPrice, city, stops)
        queue = [(0, src, 0)]
        # Dictionary to track the minimum cost to a city with up to 'stops' stops
        best = defaultdict(lambda: float('inf'))
        best[(src, 0)] = 0
        
        while queue:
            totalPrice, city, stops = heapq.heappop(queue)
            
            # If we reached the destination, return the price
            if city == dst:
                return totalPrice
            
            # If we can still make a stop
            if stops <= k:
                for toCity, price in graph[city]:
                    newPrice = totalPrice + price
                    # Proceed only if this path is cheaper
                    if newPrice < best[(toCity, stops+1)]:
                        best[(toCity, stops+1)] = newPrice
                        heapq.heappush(queue, (newPrice, toCity, stops + 1))
        
        return -1  # No valid route found within the stop limit