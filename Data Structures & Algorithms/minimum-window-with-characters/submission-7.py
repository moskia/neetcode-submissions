class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(s) < len(t)): return ""
        l = 0
        r = len(t)
        window_freq = self.frequencies(s[l:r])
        freq = self.frequencies(t)
        minL = 0
        length = float("inf")

        while r <= len(s):
            while self.contains(window_freq, freq):

                if length > r - l:
                    length = r - l
                    minL = l

                window_freq[s[l]] -= 1
                l += 1

            if r < len(s):
                window_freq[s[r]] = window_freq.get(s[r], 0) + 1

            r += 1

        if length == float("inf"):
            return ""

        return s[minL:minL+length]


    def frequencies(self, s):
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        return freq
    
    def contains(self, window_freq, freq):
        for c in freq:
            if window_freq.get(c, 0) < freq[c]:
                return False
        return True
