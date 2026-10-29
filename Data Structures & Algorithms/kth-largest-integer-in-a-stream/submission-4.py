class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hp = nums
        heapq.heapify(self.hp)
        while len(self.hp) > self.k :
            heapq.heappop(self.hp)

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        if len(self.hp) > self.k:
            heapq.heappop(self.hp)
        return self.hp[0]
