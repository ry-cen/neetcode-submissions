class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def bt(i, nums):
            if i > len(nums) - 1:
                return [[]]
            
            subsets = bt(i+1, nums)

            subsets_with = [subset + [nums[i]] for subset in subsets if subset + [nums[i]] not in subsets]

            return subsets + subsets_with

        

        return bt(0, nums)
            