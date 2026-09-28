class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT = {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        minLength = float('infinity')
        subS, l, optimalL = {}, 0, 0
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            subS[c] = subS.get(c, 0) + 1

            # check if we checked one condition of characters needed
            if c in countT and countT[c] == subS[c]:
                have += 1
            
            while have == need:
                if minLength > r-l+1:
                    minLength = r-l+1
                    optimalL = l

                subS[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > subS[s[l]]:
                    have -= 1

                l += 1
        
        return s[optimalL:optimalL+minLength] if minLength != float('infinity') else ""
