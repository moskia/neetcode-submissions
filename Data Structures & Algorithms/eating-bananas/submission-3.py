class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursTaken(k):
            return sum(((p-1)//k + 1) for p in piles)

        a, b = 1, max(piles)

        while a < b:
            k = (a+b)//2
            if hoursTaken(k) > h:
                a = k + 1
            else:
                b = k

        return a