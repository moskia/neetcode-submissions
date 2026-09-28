class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        result = []
        n = len(nums)
        for i in range(1, n):
            prefix.append(nums[i-1]*prefix[i-1])
            suffix.append(nums[n-i]*suffix[i-1])
        
        for j in range(n):
            result.append(prefix[j]*suffix[n-j-1])

        return result