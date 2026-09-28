class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myFreq = {}
        for n in nums:
            if n not in myFreq:
                myFreq[n] = 0
            myFreq[n] +=1

        result = [[] for _ in range(len(nums) + 1)]
        for key, value in myFreq.items():
            result[value].append(key)

        res = []
        for i in range(len(result) - 1, 0, -1):
            for num in result[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res