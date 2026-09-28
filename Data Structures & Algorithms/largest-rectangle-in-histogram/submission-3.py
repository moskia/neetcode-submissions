class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                start = stack[-1] if stack else -1

                maxArea = max(maxArea, (i-1-start)*height)

            stack.append(i)

        return maxArea