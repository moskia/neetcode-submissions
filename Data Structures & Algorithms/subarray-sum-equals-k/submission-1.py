class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prev_count = {0:1}
        curr_sum = 0

        for num in nums:
            curr_sum += num
            prev_sum = curr_sum - k
            count += prev_count.get(prev_sum, 0)

            prev_count[curr_sum] = prev_count.get(curr_sum, 0) + 1

        return count

            
