class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0): return 0
        l, r = 0, 0
        maxLength = 1
        char = set()
        while r < len(s):
            if s[r] not in char: 
                char.add(s[r])
                r += 1
            else:
                char.remove(s[l])
                l += 1
            maxLength = max(r-l, maxLength)
        return maxLength