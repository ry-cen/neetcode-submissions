class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def bt(i, cur, target):
            if target == 0:
                res.append(cur.copy())
                return

            if i > len(candidates) or target < 0:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > target:
                    continue

                bt(j + 1, cur + [candidates[j]], target - candidates[j])


        bt(0, [], target)

        return res