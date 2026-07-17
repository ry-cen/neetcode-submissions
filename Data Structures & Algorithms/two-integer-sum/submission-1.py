class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = defaultdict(list)
        for i, num in enumerate(nums):
            numMap[num].append(i)

        for i, num in enumerate(nums):
            req = target - num
            if req not in numMap:
                continue
            elif num == req:
                if len(numMap[req]) > 1:
                    return [i, numMap[req][1]]
            else:
                return [i, numMap[req][0]]

        return False
