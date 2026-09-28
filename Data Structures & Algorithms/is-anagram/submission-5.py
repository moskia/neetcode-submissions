class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        count_s, count_t = defaultdict(int), defaultdict(int)

        for char_s, char_t in zip(s, t):
            count_s[char_s] += 1
            count_t[char_t] += 1

        return count_s == count_t