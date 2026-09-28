class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNumb = set(nums)
        maxIter = 0

        for n in nums:
            if n-1 not in setNumb:
                r = 0
                k = n
                while k in setNumb:
                    k += 1
                    r += 1
                maxIter = max(maxIter, r)

        return maxIter