class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        max_flights = k + 1
        dist = [[sys.maxsize]*(max_flights + 1) for _ in range(n)]

        dq = []
        heapq.heappush(dq, (0, 0, src))

        while dq:
            price, curr_flights, u = heapq.heappop(dq)

            if price > dist[u][curr_flights]:
                continue

            if u == dst:
                return price

            if curr_flights >= max_flights:
                continue

            for v, p in adj[u]:
                new_flights = curr_flights + 1
                new_price = price + p
                if new_price < dist[v][new_flights]:
                    dist[v][new_flights] = new_price
                    heapq.heappush(dq, (new_price, new_flights, v))

        return -1