class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def countRec(coins, n, sum, dp):
            if sum == 0:
                return 0

            if sum < 0 or n == 0:
                return float('inf')

            if dp[sum] != 0:
                return dp[sum]

            
            
            dp[sum] = min(1 + countRec(coins, n, sum - coins[n-1], dp), countRec(coins, n-1, sum, dp))
            return dp[sum]
        
        dp = [0] * (amount + 1)

        count = countRec(coins, len(coins), amount, dp)
        
        if count == float('inf'): return - 1
        
        return count
