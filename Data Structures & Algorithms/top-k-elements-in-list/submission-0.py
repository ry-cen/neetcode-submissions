class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        buckets = [[] for _ in range(max(count.values()))]

        for key, v in count.items():
            buckets[v-1].append(key)
        res = []
        for b in reversed(buckets):
            for v in b:
                if len(res) < k:
                    res.append(v)
                else: break

        return res