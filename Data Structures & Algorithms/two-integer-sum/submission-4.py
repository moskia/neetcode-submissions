class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            elt = target - nums[i]
            if elt in dic:
                return [dic[elt], i]
            else:
                dic[nums[i]] = i

        return []