class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {};
        for i in range(len(nums)) :
            rest = target - nums[i]
            if rest in dic :
                return [dic[rest], i]
            dic[nums[i]] = i

        return []