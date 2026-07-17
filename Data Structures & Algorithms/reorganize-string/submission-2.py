class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        for key, value in counter.items():
            heapq.heappush(heap, [-value, key])
        
        res = ""
        last = None
        while heap:
            value, key = heapq.heappop(heap)
            if last == key:
                if heap:
                    tValue, tKey = value, key
                    value, key = heapq.heappop(heap)
                    res += key
                    if value < -1:
                        heapq.heappush(heap, [value + 1, key])
                    value, key = tValue, tKey
                else:
                    return ""

            res += key
            if value < -1:
                heapq.heappush(heap, [value + 1, key])
            last = key
        return res