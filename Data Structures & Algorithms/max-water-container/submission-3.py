class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxWaterAmount = min(heights[i], heights[j]) * (j - i)
        while i < j:
            if heights[i] >= heights[j]:
                j -= 1
            else:
                i += 1
            
            maxWaterAmount =  max(min(heights[i], heights[j]) * (j - i), maxWaterAmount)

        return maxWaterAmount