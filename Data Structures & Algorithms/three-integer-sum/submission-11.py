class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        t = 0

        while t < len(nums):
            left = t + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > -nums[t]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[t]:
                    left += 1
                else:
                    res.append([nums[left], nums[right], nums[t]])
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    right -= 1
                    left += 1

            while t < len(nums) - 1 and nums[t] == nums[t+1]:
                t += 1
            t += 1

        return res