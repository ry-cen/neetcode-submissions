class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        res = 0
        
        left = 0
        right = 1
        chars = set([s[left]])

        while right < len(s):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            res = max(res, right - left + 1)
            right += 1

        return res