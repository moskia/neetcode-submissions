class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        maxArea = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                l = stack[-1] if stack else -1

                maxArea = max(maxArea, (i-l-1)*height)


            stack.append(i)
        
        return maxArea