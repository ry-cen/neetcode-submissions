class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 1
        res = s[0]
        for idx, c in enumerate(s):
            left = idx
            right = idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    longest = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1

            left = idx
            right = idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    longest = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1

        return res