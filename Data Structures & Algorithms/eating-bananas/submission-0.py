class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValidSpeedEating(eat: int) -> bool:
            return sum([(p-1)//eat + 1 for p in piles]) <= h

        minSpeed, maxSpeed = 1, sum(piles)

        while minSpeed <= maxSpeed: 
            mid = (minSpeed + maxSpeed) // 2
            if isValidSpeedEating(mid):
                maxSpeed = mid - 1
            else: 
                minSpeed = mid + 1
        
        return minSpeed