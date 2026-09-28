class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        code = [0]*26
        
        for i in range(len(s)) : 
            code[ord(s[i])-ord('a')] += 1
            code[ord(t[i])-ord('a')] -= 1

        return all( v == 0 for v in code)