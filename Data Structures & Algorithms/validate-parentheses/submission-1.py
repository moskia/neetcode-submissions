class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')' : '(', ']' : '[', '}' : '{'}
        elt = []

        for c in s:
            if elt and c in dic:
                if dic[c] != elt[-1]:
                    return False
                else:
                    elt.pop()
            else:
                elt.append(c)
        
        return True if len(elt) == 0 else False