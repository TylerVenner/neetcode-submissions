class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}

        for str in strs:
            l = [0] * 26
            for c in str:
                l[ord(c) - ord('a')] += 1
            l = tuple(l)
            if l in a:
                a[l].append(str)
            else:
                a[l] = [str]

        return list(a.values())
         