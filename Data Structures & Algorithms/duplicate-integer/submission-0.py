class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnum = set(nums)

        return len(list(setnum)) < len(nums)