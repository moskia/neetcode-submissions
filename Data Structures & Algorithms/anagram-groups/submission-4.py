class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def frequency(s: str) -> str:
            freq = [0]*26
            for c in s:
                freq[ord(c)-97] += 1
            return str(freq)

        dic = {}
        for s in strs:
            freq = frequency(s)
            if freq not in dic:
                dic[freq] = []
            dic[freq].append(s)
        
        return list(dic.values())