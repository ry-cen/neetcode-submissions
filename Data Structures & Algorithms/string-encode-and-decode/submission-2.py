class Solution:

    def encode(self, strs: List[str]) -> str:
        strLens = [len(s) for s in strs]

        res = "".join(strs)
        if not strs:
            return ""
        prefix = ""
        for l in strLens:
            prefix += f"l{l}"

        res = f"{prefix}|{res}"

        return res

    def decode(self, s: str) -> List[str]:
        prefix = s[:s.find('|')]
        strings = s[s.find('|') + 1:]

        strLens = prefix.split('l')
        res = []
        index = 0
        for l in strLens[1:]:
            res.append(strings[index: index + int(l)])
            index += int(l)

        return res