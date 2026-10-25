class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def rec(i):
            best = 1
            if i in memo:
                return memo[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    best = max(best, 1 + memo[j])  
            memo[i] = best
            return best

        res = [0] * n
        for i in range(n):
            res[i] = rec(i)

        return max(res)
        