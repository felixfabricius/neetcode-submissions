"""
Solution approaches:
1) Double for loop over all the characters. O(n^2) time, O(1) space
2) 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first_occurences = {}
        longest_substring = 0
        recent_substring = 0
        for i in range(len(s) - 1, -1, -1):
            if first_occurences.get(s[i], len(s)) - i >= recent_substring + 1:
                recent_substring += 1
            else:
                recent_substring = first_occurences[s[i]] - i
                # This part is very important. I had initially forgotten to write this.
            longest_substring = max(longest_substring, recent_substring)
            first_occurences[s[i]] = i
        return longest_substring
        