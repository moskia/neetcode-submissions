class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        frequency = [[] for i in range(len(nums)+1)]
        for num in nums:
            dic[num] += 1
        
        for key, val in dic.items():
            frequency[val].append(key)

        
        result = []
        n = len(frequency)
        for i in range(n):
            for elt in frequency[n-i-1]:
                result.append(elt)
                if len(result) == k:
                    return result