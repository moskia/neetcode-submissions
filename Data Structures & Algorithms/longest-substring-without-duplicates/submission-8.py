class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        elts = set()

        while r < len(s):
            if s[r] not in elts: 
                elts.add(s[r])
                r += 1
            elif s[l] in elts: 
                elts.remove(s[l])
                l +=1

            res = max(res, r-l)

            
        return res  