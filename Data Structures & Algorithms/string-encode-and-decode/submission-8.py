class Solution:

    def encode(self, strs: List[str]) -> str:
        # First find a possible delimiter symbol
        used_sequences = set()
        for string in strs:
            if len(string) < 2:
                continue
            for i in range(1, len(string)):
                used_sequences |= set(string[i-1:i+1])
            used_sequences |= set(string)

        delimiter = ""
        for i in range(0, 256):
            if delimiter:
                break
            for j in range(0, 256):
                if chr(i) + chr(j) not in used_sequences:
                    delimiter = chr(i) + chr(j)
                    print(delimiter)
                    break # issue: need to break out of double for-loop! (for efficiency)
        
        # Issue: this above way can create delimiters that don't have length(2). Because characters also include
        # things that actually don't look like a character, i.e. aren't alphanumerical.


        delimiter = "z2"
        #assert len(delimiter) == 2
        output = ""
        for i, string in enumerate(strs):
            output += delimiter
            output += string
        
        return output        

    def decode(self, s: str) -> List[str]:
        print(s)
        delimiter = s[:2]
        if not delimiter:
            return []
        beginnings = []
        for i in range(2, len(s) + 1):
            if s[i-2:i] == delimiter:
                beginnings.append(i)
        print(beginnings)
        print(delimiter)
        output = []
        for i, beginning in enumerate(beginnings):
            if i + 1 == len(beginnings):
                output.append(s[beginning:])
                return output
            end = beginnings[i + 1] - 3 # -3: -> end is inclusive index
            output.append(s[beginning: end + 1])

        raise RuntimeError("unreachable code part reached")