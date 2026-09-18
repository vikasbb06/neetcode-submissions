from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a dictionary where the default value is an empty list
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to use as a unique key
            sorted_key = "".join(sorted(s))
            # Append the original string to its matching key
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())
