class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        need, have = len(countT), 0
        l = 0
        optimalL, minLength = 0, float('infinity')

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need: 
                if (r-l+1) < minLength:
                    minLength = r-l+1
                    optimalL = l
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l +=1
        return s[optimalL:optimalL+minLength] if minLength != float('infinity') else ""