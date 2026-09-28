class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        frequency = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1

        for key, value in dic.items():
            frequency[value].append(key)

        res = []
        for j in range(len(frequency)-1, -1, -1):
            for l in range(len(frequency[j])):
                res.append(frequency[j][l])
                if len(res) == k:
                    return res

