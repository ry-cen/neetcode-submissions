class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]

        heapq.heapify(nums)
        res = []
        for _ in range(k):
            res.append(-heapq.heappop(nums))

        return res[-1]