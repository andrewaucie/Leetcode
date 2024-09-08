class Solution:
    def findItinerary(self, tickets) -> list[str]:
        # Initialize the flight graph using ticket information
        flightGraph = defaultdict(list)
        travelItinerary = []

        for ticket in tickets:
            fromAirport, toAirport = ticket[0], ticket[1]
            flightGraph[fromAirport].append(toAirport)

        # Sort destinations in reverse order to visit lexical smaller destinations first
        for destinations in flightGraph.values():
            destinations.sort(reverse=True)

        dfsStack = ["JFK"]

        while dfsStack:
            # Get the current airport from the top of the stack
            currentAirport = dfsStack[-1]
            destinations = flightGraph.get(currentAirport, [])

            if destinations:
                # Choose the next destination (the one in lexicographically larger order)
                nextDestination = destinations.pop()
                dfsStack.append(nextDestination)
            else:
                # If there are no more destinations from the current airport, add it to the itinerary
                travelItinerary.append(currentAirport)
                dfsStack.pop()

        # Reverse the itinerary to get the correct order
        travelItinerary.reverse()
        return travelItinerary