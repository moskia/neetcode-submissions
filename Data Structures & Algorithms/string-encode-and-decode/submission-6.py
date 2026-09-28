class Solution:

    def encode(self, strs: List[str]) -> str:
        enCode = ""
        for s in strs:
            enCode += str(len(s)) + ","
        enCode += "#" + ''.join(strs)
        return enCode


    def decode(self, s: str) -> List[str]:
        result = []
        length = []
        l = ""
        for i in range(len(s)):
            if s[i] == "#":
                s = s[i+1:]
                break
            if s[i] != ",":
                l += s[i]
            else:
                length.append(int(l))
                l = ""
                continue

        j = 0
        n = 0
        for i in length:
            c = ""
            n += i
            while j < n:
                c += s[j]
                j += 1
            result.append(c)
        return result
