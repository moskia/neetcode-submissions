class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(s.lower().split(" "))
        res = ""
        for c in text:
            if (ord(c) >= 97 and ord(c) < 123) or c in "0123456789":
                res += c
        print(res)
        left = 0
        right = len(res) - 1
        while left < right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1

        return True