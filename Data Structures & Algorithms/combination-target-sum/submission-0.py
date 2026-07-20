class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(i, cur, target):
            if target == 0:
                res.append(cur.copy())

            if i >= len(nums) or target < 0:
                return

            for j in range(i, len(nums)):
                if nums[j] > target:
                    continue
                backtracking(j, cur + [nums[j]], target - nums[j])

        backtracking(0, [], target)

        return res