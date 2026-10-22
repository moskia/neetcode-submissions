class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for s, d, w in flights:
            adj[s].append((d, w))

        max_flights = k+1

        dist = [[sys.maxsize]*(max_flights+1) for _ in range(n)]
        dist[src][0] = 0

        dq = []
        heapq.heappush(dq, (0, 0, src))

        while dq:
            cost, flights_used, u = heapq.heappop(dq)

            if dist[u][flights_used] < cost:
                continue

            if u == dst:
                return cost

            if flights_used >= max_flights:
                continue

            for v, price in adj[u]:
                new_flights = flights_used + 1
                new_cost = price + cost
                if new_cost < dist[v][new_flights]:
                    dist[v][new_flights] = new_cost
                    heapq.heappush(dq, (new_cost, new_flights, v))

        return -1
