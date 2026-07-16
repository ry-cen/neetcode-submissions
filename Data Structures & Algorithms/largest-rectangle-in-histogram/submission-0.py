class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        heights.append(0)
        heightStack = deque()
        res = 0
        for i in range(n+1):
            while heightStack and (i == n or heights[heightStack[-1]] >= heights[i]):
                height = heights[heightStack.pop()]
                width = i if not heightStack else i - heightStack[-1] - 1
                res = max(res, height * width)

            heightStack.append(i)

        return res