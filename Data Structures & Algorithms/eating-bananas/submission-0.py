class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        mmax = max(piles)
        l = 1
        r = mmax

        def canEatAll(speed):
            res = 0
            for p in piles:
                res += math.ceil(p/speed)
            return res <= h

        res = mmax

        while l < r:
            mid = l + (r-l)//2
            if canEatAll(mid):
                res = min(res, mid)
                r = mid
            else:
                l = mid + 1
        
        return res