class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = suffix = 0
        res = -float('inf')

        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[-i-1] * (suffix or 1)
            res = max(res, max(prefix, suffix))

        return res