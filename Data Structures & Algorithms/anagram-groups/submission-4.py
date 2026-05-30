import string

class Solution:    
    """
    Solution 1:
    1) For each string, store the string components (O(mk) time and space), 
       where m is number of inputs & k is average length of string
    2) Do pairwise comparison of all of the string components. If they match, group together.
       Can do this in a smart way to reduce constant factors. 
       E.g. also store length of string as one of the components (not just the character make-up), 
       & then first compare the length.
       Time complexity of this: O(m^2) comparisions, and each comparison takes O(k).
       (It's not immediately obvious that each comparison takes O(k).
       Reason: there is variation in string lengths. 
       But note that each comparison complexity is upper bound by min(k_1, k_2) + 1, where k_1 and k_2
       are word lengths of the two words we compare)
    Total complexity:
    - Time: O(mk) + O(m^2k) = O(m^2k)
    - Space: O(mk) + O(mk) (for the latter we assume that storing a word of length k is O(k))

    What's intuitively inefficient about this solution? The pairwise comparison loop.

    Instead, let's try create a hash table.
    Approach:
    1) Use hash function to map from word to dictionary key. h(a) == h(b) <=> a and b are anagrams
       - Option 1 (based on solutions): sort the characters. key = "".join(sorted(s))
         (This is O(m log m))
       - Option 2 (my idea): create some array or string that records occurences of each character.
         String does not work, because not mutable. Integer arithmetic would be very memory intensive.
         Better: take a mutable array (e.g. list), and then convert to something immutable (tuple).
         This takes O(m)

    2) Then let values in the dictionary be lists (dynamic arrays). Append words. 
    3) To return: list(dict.values()) (this is O(n), where n is number of dict keys). 
       (The reason this is O(n) and independent of hwo complex "values" is, is that Python 
       does not create a copy of the actual values, but just stores references to where they
       are saved in that dictionary.)
    """
    def hash_func(self, s):
        """
        # Need a map from character to position; recall that 0 is len
        {
            "a": 1,
            "b": 2,
            "c": 3, 
            "d": 4, 
            ...
        }
        """
        """
        This doesn't work because strings don't support item assignment.
        Using an integer (arithmetic based on powers of 10) also seems unideal, cause
        then we get absolutely massive integers, which Python might not like. 

        char_to_idx = {string.ascii_lowercase[i]: i + 1 for i in range(0, 26)}
        h = str(len(string)) + ("0" * 26)
        for char in string:
            h[char_to_idx[char]] = str(int(h[char_to_idx[char]]) + 1)
        """
        char_to_idx = {string.ascii_lowercase[i]: i for i in range(0, 26)}
        h = [0] * 26
        for char in s:
            h[char_to_idx[char]] += 1
        return tuple(h) 
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[Tuple[int], List[str]] = {}
        for s in strs:
            h = self.hash_func(s)
            groups[h] = groups.get(h, []) + [s]
        return list(groups.values())


        

