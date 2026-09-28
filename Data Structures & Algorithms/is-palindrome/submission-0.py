class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = ""
        n = len(s)
        for i in range(n):
            if (ord(s[i]) <= ord('z') and ord(s[i]) >= ord('a')) or (ord(s[i]) <= ord('Z') and ord(s[i]) >= ord('A')) or (ord(s[i]) <= ord('9') and ord(s[i]) >= ord('0')): 
                t += s[i]

        m = len(t)
        for i in range(m//2):
            if(t[i] != t[m-i-1]): return False
        
        return True