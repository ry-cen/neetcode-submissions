class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(i, nums):
            if i > len(nums) - 1:
                return [[]]

            
            return [combo + [nums[j]] for combo in bt(i + 1, nums) for j in range(len(nums)) if nums[j] not in combo]

        return bt(0, nums)