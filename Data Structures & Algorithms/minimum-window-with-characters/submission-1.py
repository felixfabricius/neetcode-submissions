class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        chars = {}
        
        # O(n)
        for char in t:
            if char in chars:
                chars[char][0] += 1
            else:
                chars[char] = [1, deque()]

        # 
        n_incomplete = len(chars)

        for i in range(len(s)):
            if s[i] not in chars:
                continue
            if len(chars[s[i]][1]) < chars[s[i]][0]:
                chars[s[i]][1].append(i)

                # First time we 
                if len(chars[s[i]][1]) == chars[s[i]][0]:
                    n_incomplete -= 1
                    if n_incomplete == 0:
                        complete_substring_start = len(s)
                        for char in chars:
                            complete_substring_start = min(complete_substring_start, chars[char][1][0])
                        complete_substring_end = i + 1
            else:
                chars[s[i]][1].popleft()
                chars[s[i]][1].append(i)

                # Check if this yields a shorter complete substring: 
                # O(m) because we perform O(1) operation for each unique character in t
                # to see where the substring starts.
                # This could be reduced to O(log m) by keeping track of a tree which stores 
                # for each character, the index of the earliest character to achieve streak.
                if n_incomplete == 0:
                    candidate_complete_substring_start = len(s)
                    for char in chars:
                        candidate_complete_substring_start = min(candidate_complete_substring_start, chars[char][1][0])
                    if i + 1 - candidate_complete_substring_start < complete_substring_end - complete_substring_start:
                        complete_substring_start = candidate_complete_substring_start
                        complete_substring_end = i + 1
                
        if n_incomplete > 0:
            return ""
        
        return s[complete_substring_start:complete_substring_end]

        # Suppose that all our queues are already of required length
        # And we know the start of the currently shortest
        # And then length of the currently shortest substring
        # If we add a new character, i.e. replace in one of the queues
        # How can we determine if this pushes start of currently shortest substring back?
            # If we need to scan through all the unique characters, complexity becomes O(n*m)
        # So would also need to maintain some data structure that tracks earliest current value
        # for each of the characters we need, and where we can quickly check if the current character
        # has the smallest earliest value.
            # For this use case, heap initially seems like good idea.
            # However, also need to update the earliest current value for characters which don't have the
            # earliest "earliest current value". And this is not efficient with a heap:
            # O(m) since we need to loop through everything.
            # Binary tree would be O(log m)
        # Even so, we'd have:
            # Space: 
                # O(len(t)) < O(len(s)) = O(n) for keeping track of the queus
                # O(m) for maintaining the tree
            # Time:
                # initial scan through characters in t to get number needed: O(n)
                # For each of the n characters in s:
                    # update the queues O(1)
                    # update the tree O(log m)
                # -> O(n log m)


        # Scan through s and adequately modify queues        
