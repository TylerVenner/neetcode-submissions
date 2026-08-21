class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for word in strs:
            # Build a count of 26 lowercase letters
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            # Use the tuple of counts as a key
            key = tuple(count)
            
            if key in anagram_map:
                anagram_map[key].append(word)
            else:
                anagram_map[key] = [word]
        
        return list(anagram_map.values())
