"""
Data Structure:
- build a tree, where each node is a character, in order
- for each character store a hash map with next character and the 
  node of that next character

Search:
- use DFS to account for '.': if '.', then go through all possible next characters.
  can perhaps call search recursively.

Complexity of what I'm doing:
- addWord: O(length of word); for each character, doing a constant time operation
- search: 
  time: without any dots, we do constant number of constant time operations for each character -> O(len of word total)
  with the dots and the DFS: go down each possible branch; O(X) time
  might be able to reduce if we can use union more effectively
  space complexity: only going down one branch at a time -> O(len of word for recursion stack)
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
                    #return sum([dfs(prev, char + remaining_word) for char in prev.children]) >= 1
                    # Interested in union of all possible branches
                    # Challenge when coding this: not sure how many branches there are.
                    # -> I went for this.
                    # Better: use generator version of any(), which can stop early if it finds a match!!!
                    return any(dfs(prev, char + remaining_word) for char in prev.children)           
        
        return dfs(self.root, word + "E")
        
