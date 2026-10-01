class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)): return False
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if self.frequencies(s1) != self.frequencies(s2[l:r+1]):
                r += 1
                l += 1
            else:
                return True

        return False

    def frequencies(self, s):
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        return freq