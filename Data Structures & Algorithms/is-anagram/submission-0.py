class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # this is O(1) check that might improve constant factors
        
        s_chars = {}
        t_chars = {}

        for char in s:
            if char in s_chars: 
                s_chars[char] += 1
            else: 
                s_chars[char] = 1
        
        for char in t:
            if char in t_chars:
                t_chars[char] += 1
            else:
                t_chars[char] = 1
        
        # Check if the two dictionaries are equal
        for char in set(s_chars.keys()).union(t_chars.keys()):
            if s_chars.get(char) != t_chars.get(char):
                return False
        return True