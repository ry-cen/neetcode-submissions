class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combo = deque()
        def bt(openP, closeP):
            if openP == n and closeP == n:
                res.append("".join(combo))
                return

            if openP < n:
                combo.append("(")
                bt(openP + 1, closeP)
                combo.pop()

            if closeP < openP:
                combo.append(")")
                bt(openP, closeP + 1)
                combo.pop()



        bt(0, 0)
        return res