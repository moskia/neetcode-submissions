class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, w in times:
            adj[u - 1].append((v - 1, w))

        pq = []
        dist = [sys.maxsize] * n

        dist[k-1] = 0
        heapq.heappush(pq, (0, k-1))

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        if sys.maxsize in dist:
            return -1

        return max(dist)
        