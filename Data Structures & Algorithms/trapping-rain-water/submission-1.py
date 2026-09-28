class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pMax = [height[-1]]
        for i in range(n-2, -1, -1):
            pMax.append(max(height[i], pMax[-1]))

        sMax = [height[0]]
        for j in range(1, n):
            sMax.append(max(height[j], sMax[-1]))
        
        globArea = 0
        for l in range(n):
            globArea += min(sMax[l], pMax[n-l-1]) - height[l]
        
        return globArea