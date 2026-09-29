class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        leftMax = []
        rightMax = []
        Area = 0

        for i in range(len(height)):
            if i == 0:
                leftMax.append(0)
                rightMax.append(0)
            else:
                leftMax.append(max(leftMax[-1], height[i-1]))
                rightMax.append(max(rightMax[-1], height[len(height)-i]))

        for i in range(len(height)):
            currArea = min(leftMax[i], rightMax[len(height)-1-i]) - height[i]
            if currArea > 0:
                Area += currArea
        
        return Area
            
