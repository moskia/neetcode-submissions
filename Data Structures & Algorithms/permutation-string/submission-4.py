class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Frequency = defaultdict(int)
        for c in s1 :
            s1Frequency[c] += 1

        l = 0
        s2Frequency = defaultdict(int)
        for r in range(len(s2)):
            s2Frequency[s2[r]] += 1
            while self.contains(s2Frequency, s1Frequency):
                if len(s2[l:r+1]) == len(s1):
                    return True

                s2Frequency[s2[l]] -= 1
                l += 1

        return False

    def contains(self, dic1: defaultdict[str, int], dic2: defaultdict[str, int]) -> bool:
        for k, v in dic2.items():
            if dic1[k] < v:
                return False

        return True
