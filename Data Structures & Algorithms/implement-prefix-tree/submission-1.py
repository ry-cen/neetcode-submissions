class Node:
    def __init__(self, val=None, children={}):
        self.val = val
        self.children = children

class PrefixTree:

    def __init__(self):
        self.root = Node(' ', {})

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word + '#':
            if c not in curr.children.keys():
                curr.children[c] = Node(c, {})
            curr = curr.children[c]

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word + '#':
            curr = curr.children.get(c)
            if not curr:
                return False

        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            curr = curr.children.get(c)
            if not curr:
                return False

        return True
        
        