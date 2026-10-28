class Solution:
    def jump(self, nums: List[int]) -> int:
        jp = nums[0]
        pos = 0
        count = 0
        n = len(nums)
        while pos < n-1:
            curr = pos
            if pos + jp >= n-1:
                count += 1
                pos = n-1
                break
            sub = nums[pos+1:pos+jp+1]
            for i in range(len(sub)):
                sub[i] = sub[i] + i

            m = max(sub)

            indices = [i for i, x in enumerate(sub) if x == m]
            pos = pos + 1 + indices[-1]

            jp = nums[pos]
            count += 1

        return count