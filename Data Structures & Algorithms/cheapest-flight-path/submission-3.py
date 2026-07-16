class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        queue = []

        res = float('inf')

        adjList = defaultdict(list)
        for flight in flights:
            adjList[flight[0]].append([flight[1], flight[2]])

        heapq.heappush(queue, [0, -1, src])
        while queue:
            cost, stops, curr = heapq.heappop(queue)

            if stops > k or cost > res:
                continue

            if curr == dst:
                res = min(res, cost)

            nextStops = adjList[curr]

            for stop, nextCost in nextStops:
                heapq.heappush(queue, [cost + nextCost, stops + 1, stop])

        if res == float('inf'):
            res = -1

        return res