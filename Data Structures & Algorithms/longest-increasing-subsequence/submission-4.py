from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            pos = bisect_left(tails, num)

            # TODO: What if pos is at the end of tails?
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)
