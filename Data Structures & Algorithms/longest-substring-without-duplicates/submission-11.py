class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        l, r = 0, 0
        maxLength = 0
        currLength = 0
        while r < len(s):
            
            while s[r] in my_set:
                my_set.remove(s[l])
                currLength -= 1
                l += 1
                
            my_set.add(s[r])
            currLength += 1
            maxLength = max(maxLength, currLength)
            r += 1

        return maxLength
