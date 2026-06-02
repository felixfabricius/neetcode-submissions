class Solution:
    def isValid(self, s: str) -> bool:
        """
        Potential solutions:
        1)  Two pointers. O(n) time, O(1) space.
            Nvm, this doesn't work. Word does not need to be a
            palindrome!
        2)  Keep track of a running tally. 
            For each bracket type, 
            +1 if opening bracket, -1 if closing bracket.
            Valid if 
            - sum is zero at end for every bracket type
            - and sum is never negative for any bracket type
            O(n) time, O(1) space.
            But this also doesn't work because it doesn't 
            take into consideration whether opening brackets 
            are closed in the correct order or not.
        3)  Idea: use stacks!
            For each closing bracket we encounter, check that the
            last opening bracket was of the corresponding type.
            Fail if:
            - There is a closing bracket for which we cannot close a
              corresponding opening bracket
            - After all the closing brackets, there are still opening brackets
              left
        """
        opening_stack = []
        mp = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in mp:
                if (
                    len(opening_stack) == 0 
                    or opening_stack.pop() != mp[char]
                ):
                    return False
            else:
                opening_stack.append(char)
        
        if len(opening_stack) != 0:
            return False
        
        return True
