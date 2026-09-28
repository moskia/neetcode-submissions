class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def frequency(s: str) -> str:
            code = [0] * 26
            for i in range(len(s)):
                code[ord(s[i])-97] += 1

            return str(code)

        mydict = {}
        for s in strs:
            freq = frequency(s)

            if freq not in mydict:
                mydict[freq] = []
            mydict[freq].append(s)

        return list(mydict.values())