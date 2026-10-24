class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climb(n, dp):
            if n == 1:
                return 1
            if n == 0:
                return 1

            if dp[n] != 0:
                return dp[n]
            
            dp[n] = climb(n-1, dp) + climb(n-2, dp)
            return dp[n]
        
        dp = [0] * (n+1)
        
        return climb(n, dp)