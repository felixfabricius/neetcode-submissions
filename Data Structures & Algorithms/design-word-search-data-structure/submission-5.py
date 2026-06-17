"""
Data Structure:
- build a tree, where each node is a character, in order
- for each character store a hash map with next character and the 
  node of that next character

Search:
- use DFS to account for '.': if '.', then go through all possible next characters.
  can perhaps call search recursively.
"""

class TreeNode:
    def __init__(self, children: dict[str, TreeNode] | None = None):
        self.children = children if children else {}

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        prev = self.root
        for char in word + "E":
            if not char in prev.children:
                prev.children[char] = TreeNode()
            prev = prev.children[char]

    def search(self, word: str) -> bool:
        def dfs(prev: TreeNode, word: str) -> bool:
            for i in range(len(word)):
                #print(f"word: {word}; prev.children: {prev.children.keys()}; current char: {word[i]}")
                char = word[i]
                if (
                    char != "." and char not in prev.children
                    #or (char == "." and len(prev.children) == 0)
                ):
                    return False
                elif char == "E" and i == len(word) - 1:
                    # The second part here is an important guard against the
                    # case where we have multiple . at the end of our word, and
                    # we then effectively 'reuse' the E from our tree 
                    return True
                elif char != ".":
                    prev = prev.children[char]
                else: 
                    # char == "."
                    # 
                    remaining_word = word[i + 1: ] if len(word) > i else ""
                    return sum([dfs(prev, char + remaining_word) for char in prev.children]) >= 1
                    # Interested in union of all possible branches
                    # Challenge when coding this: not sure how many branches there are.
                    # -> I went for this.           
        
        return dfs(self.root, word + "E")
        
