class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) > len(self.right):
            if not self.right:
                if num >= -self.left[0]:
                    heapq.heappush(self.right, num)
                else:
                    tmp = heapq.heappop(self.left)
                    heapq.heappush(self.right, -tmp)
                    heapq.heappush(self.left, -num)
            elif num >= -self.left[0]:
                heapq.heappush(self.right, num)
            else:
                tmp = heapq.heappop(self.left)
                heapq.heappush(self.right, -tmp)
                heapq.heappush(self.left, -num)

        else:
            if not self.left:
                heapq.heappush(self.left, -num)
            elif num <= self.right[0]:
                heapq.heappush(self.left, -num)
            else:
                tmp = heapq.heappop(self.right)
                heapq.heappush(self.left, -tmp)
                heapq.heappush(self.right, num)


    def findMedian(self) -> float:
        print(self.left)
        print(self.right)
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2
        