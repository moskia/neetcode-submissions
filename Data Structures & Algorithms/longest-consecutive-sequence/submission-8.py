class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0): return 0
        s = set(nums)
        longSeq = 1

        for num in nums: 
            if (num-1) not in s: 
                length = 0
                while num+length in s:
                    length += 1
                longSeq = max(longSeq, length)

        return longSeq