class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for str in strs:
            l = [0] * 26

            for char in str:
                l[ord(char) - ord('a')] += 1

            if tuple(l) in d:
                d[tuple(l)].append(str)
            else:
                d[tuple(l)] = [str]

        
        return list(d.values())

