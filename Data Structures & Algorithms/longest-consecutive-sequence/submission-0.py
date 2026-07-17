class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in nums:
            if num-1 not in numset:
                target = num + 1
                pres = 1
                while target in numset:
                    pres += 1
                    target += 1

                res = max(res, pres)

        return res