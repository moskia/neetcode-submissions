class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        frequency = [[] for i in range(len(nums)+1)]
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        
        for key, value in freq.items():
            frequency[value].append(key)

        res = []
        for i in range(len(frequency)-1, -1, -1):
            for j in range(len(frequency[i])):
                res.append(frequency[i][j])
                if len(res) == k:
                    return res
