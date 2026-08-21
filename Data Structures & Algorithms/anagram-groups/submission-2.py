class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for word in strs:
            l = [0] * 26
            for char in word:
                l[ord(char) - ord("a")] += 1
            
            l = tuple(l)
            if l in h:
                h[l].append(word)
            else:
                h[l] = [word]

        return list(h.values())