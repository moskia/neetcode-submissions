class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(eat: int) -> int:
            return sum([(p-1)//eat + 1 for p in piles]) <= h

        l, r = 1, max(piles)

        while l < r:
            mid = (l+r)//2

            if isValid(mid):
                r = mid 
            else:
                l = mid + 1

        return l