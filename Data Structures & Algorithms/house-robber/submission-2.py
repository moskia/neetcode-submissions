class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (len(nums) + 1)

        def rec(nums, i):
            if i < 0:
                return 0

            if dp[i] != -1:
                return dp[i]    

            dp[i] = max(nums[i] + rec(nums, i-2), rec(nums, i-1))

            return dp[i]
            
        return rec(nums, n-1)
