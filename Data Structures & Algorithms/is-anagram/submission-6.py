class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        code  = [0]*26

        for i in range(len(s)):
            code[ord(s[i])-97] += 1
            code[ord(t[i])-97] -= 1
        
        return all(val ==  0 for val in code)
        