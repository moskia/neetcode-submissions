class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda interval: interval[1])
        n = len(intervals)
        dp = [0] * n
        last_end = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] < last_end:
                dp[i] += dp[i-1] + 1
            else:
                dp[i] = dp[i-1]
                last_end = intervals[i][1]

        return dp[-1]