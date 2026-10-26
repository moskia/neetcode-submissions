class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)

        if n1 < n2:
            n1, n2 = n2, n1
            text1, text2 = text2, text1
        
        prev = [0] * (n2+1)

        for i in range(1, n1+1):
            curr = [0] * (n2+1)
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr

        
        return prev[n2]
