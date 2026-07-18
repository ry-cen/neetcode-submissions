class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        k = len(s1)
        s1Count = Counter(s1)

        l = 0
        
        for r in range(len(s2)):
            count[s2[r]] = 1 + count.get(s2[r], 0)

            while r - l + 1 > k:
                count[s2[l]] -= 1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l += 1

            if count == s1Count:
                return True

        return False