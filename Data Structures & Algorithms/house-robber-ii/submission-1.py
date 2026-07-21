class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1 = [0] * (len(nums) - 1)
        dp2 = [0] * (len(nums))
        dp1[0] = nums[0]
        dp2[1] = nums[1]
        for i in range(1, len(dp1)):
            if i < 2:
                dp1[i] = max(nums[i], nums[i-1])
            else:
                dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])

        for i in range(2, len(dp2)):
            if i < 3:
                dp2[i] = max(nums[i], nums[i-1])
            else:
                dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1])

        return max(dp1[-1], dp2[-1])