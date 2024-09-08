class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create graph based on tickets
        graph = defaultdict(list)
        remainingTickets = defaultdict(int)
        tickets.sort()
        for depart, arrive in tickets:
            graph[depart].append(arrive)
            remainingTickets[(depart,arrive)] += 1
        
        ticketPaths = []
        # Run dfs. Track visited edges, current path, current airport
        def dfs(airport, remaining, curr):
            if len(curr) / 3 == len(tickets):
                ticketPaths.append(curr)
                return True
            visited = set()
            for arrive in graph[airport]:
                if remaining[(airport, arrive)] > 0 and (airport, arrive) not in visited:
                    visited.add((airport, arrive))
                    remaining[(airport, arrive)] -= 1
                    if dfs(arrive, remaining, curr + arrive):
                        return True
                    remaining[(airport, arrive)] += 1
            return False

        # Call dfs on "JFK"
        dfs("JFK", remainingTickets, "")
        if len(ticketPaths) == 0:
            return []
        ticketPaths.sort()
        lowest = ticketPaths[0]
        res = ["JFK"]
        for i in range(0, len(lowest), 3):
            res.append(lowest[i:i+3])
        return res