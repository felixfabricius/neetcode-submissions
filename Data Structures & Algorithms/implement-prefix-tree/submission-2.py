"""
Improvements:

"""

class PrefixTreeNode:
    def __init__(self, val: str | None = None, after: dict | None = None):
        self.val = val
        self.after = after if after is not None else {}

    def add_after(self, after_to_add: dict[str, PrefixTreeNode]) -> None:
        self.after |= after_to_add


class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word + "E":
            if char in curr.after:
                curr = curr.after[char]
            else:
                new_node = PrefixTreeNode(char)
                curr.add_after({char: new_node})
                curr = new_node

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word + "E":
            if char not in curr.after:
                return False
            curr = curr.after[char]
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.after:
                return False
            curr = curr.after[char]
        return True
        