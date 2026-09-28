class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            n = len(s)
            res += str(n) + ","
        
        return res + "#" + "".join(strs)


    def decode(self, s: str) -> List[str]:
        print(s)
        lengths = []
        length = ""
        i = 0
        while s[i] != "#":  
            if s[i] == ",":
                lengths.append(int(length))
                length = ""
            else: 
                length += s[i]
            i += 1

        print(lengths)
        res = []
        i += 1
        for j in range(len(lengths)):
            word = ""
            l = i
            while i < l + lengths[j]:
                word += s[i]
                i += 1
            res.append(word)

        return res
