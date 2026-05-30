class Solution:    
    def compare_components(self, a: Dict[str, int], b: Dict[str, int]):
        #if a["len"] != b["len"]:
        #    return False
        for char in set(a.keys()).union(b.keys()):
            if a.get(char) != b.get(char):
                return False
        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Identify characters each of the words contain
        strings_components: List[Dict[str, int]] = []
        for string in strs:
            string_component = {"len": len(string)}
            for char in string:
                string_component[char] = string_component.get(char, 0) + 1
            strings_components.append(string_component)

        assigned = set()
        anagram_lists = []

        for i in range(len(strs)):
            if strs[i] in assigned:
                continue
            
            anagram_group = [strs[i]]
            
            if i == len(strs):
                anagram_lists.append(anagram_group)
                return anagram_lists
            
            for j in range(i + 1, len(strs)):
                if self.compare_components(strings_components[i], strings_components[j]):
                    anagram_group.append(strs[j])
                    assigned.add(strs[j])
                # Note that it is not necessary to add strs[i] to assigned set.
                # Reason: this would only matter if strs[i] will appear another time later on.
                # But in that case, it will be added to assigned anyways.
            anagram_lists.append(anagram_group)
        return anagram_lists
                 


        

