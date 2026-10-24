class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * n for _ in range(amount+1)]

        def rec(i, sum):
            if sum == amount:
                return 1

            if i < 0 or sum > amount:
                return 0
            
            if dp[sum][i]!= -1:
                return dp[sum][i]

            dp[sum][i] = rec(i, sum + coins[i]) + rec(i-1, sum)
            return dp[sum][i]

        return rec(n-1, 0)
