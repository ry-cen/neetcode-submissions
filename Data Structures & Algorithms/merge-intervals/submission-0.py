class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals, key=lambda x: x[0])

        left = sortedIntervals[0][0]
        right = sortedIntervals[0][1]

        res = []

        for i in range(1, len(intervals)):
            if sortedIntervals[i][0] <= right:
                if sortedIntervals[i][1] > right:
                    right = sortedIntervals[i][1]
                else:
                    continue

            elif sortedIntervals[i][0] > right:
                res.append([left, right])
                left = sortedIntervals[i][0]
                right = sortedIntervals[i][1]

        res.append([left, right])
        return res