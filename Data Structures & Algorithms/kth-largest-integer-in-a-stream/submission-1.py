import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kthLargest = nums
        self.k = k
        heapq.heapify(self.kthLargest)
        while len(self.kthLargest) > k:
            heapq.heappop(self.kthLargest)

    def add(self, val: int) -> int:
        heapq.heappush(self.kthLargest, val)
        if len(self.kthLargest) > self.k:
            heapq.heappop(self.kthLargest)
        return self.kthLargest[0]
