class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                start, height = stack.pop()
                maxArea = max(maxArea, (i-start)*height)

            stack.append([start, h])

        return maxArea

