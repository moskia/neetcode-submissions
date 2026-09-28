class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        t = 0

        for t in range(len(nums)):
            if t > 0 and nums[t] == nums[t-1]:
                continue
            left = t + 1
            right = len(nums) - 1

            while left < right:
                target = nums[left] + nums[right] + nums[t]
                if target > 0:
                    right -= 1
                elif target < 0:
                    left += 1
                else:
                    res.append([nums[left], nums[right], nums[t]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return res