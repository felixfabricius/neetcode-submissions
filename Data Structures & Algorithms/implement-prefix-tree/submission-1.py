class PrefixTreeNode:
    def __init__(self, val: str | None = None, after: dict | None = None):
        self.val = val
        self.after = after if after is not None else {}

    def add_after(self, after_to_add: dict[str, PrefixTreeNode]):
        self.after |= after_to_add


class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        # Traverse trie, and if character does not exist, then add character
        curr = self.root
        for char in word + "E":
            if char in curr.after:
                curr = curr.after[char]
            else:
                new_node = PrefixTreeNode(char)
                curr.add_after({char: new_node})
                curr = new_node

    def search(self, word: str) -> bool:
        #print(f"\nSearch for {word}")
        curr = self.root
        i = 0
        for char in word + "E":
            #print(f"Position {i}")
            #print(f"  Char {char} in curr.after: {char in curr.after}")
            #print(f"  len(curr.after): {len(curr.after)}")
            #print(f"  curr.after: {curr.after.items()}")
            if char not in curr.after:
                return False
            curr = curr.after[char]
            i += 1
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.after:
                return False
            curr = curr.after[char]
        return True
        