import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, i):
            if i > len(nums) - 1:
                return [[]]
            combos = backtrack(nums, i + 1)
            new_combos = []
            for combo in combos:
                new_combos.append(combo + [nums[i]])
            return combos + new_combos

        return backtrack(nums, 0)