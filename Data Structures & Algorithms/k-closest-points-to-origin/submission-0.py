class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[x**2 + y**2, x, y] for x, y in points]

        heapq.heapify(distances)
        res = []

        for _ in range(k):
            dis, x, y = heapq.heappop(distances)
            res.append([x, y])
        return res
