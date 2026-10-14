class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def condition(c):
            count = 1
            k = c
            for i in range(len(weights)):
                if k < weights[i]:
                    count += 1
                    k = c
                
                k -= weights[i]
            return count > days
                

        a, b = max(weights), sum(weights)

        while a < b:
            mid = (a+b)//2
            if condition(mid):
                a = mid + 1
            else:
                b = mid

        return b