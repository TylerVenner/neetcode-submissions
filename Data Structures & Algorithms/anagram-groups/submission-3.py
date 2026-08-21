class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = {}
        for str in strs:
            l = [0] * 26
            for char in str:
                l[ord(char) - ord('a')] += 1

            l = tuple(l)
            if l in h:
                h[l].append(str)
            else:
                h[l] = [str]

        return list(h.values())