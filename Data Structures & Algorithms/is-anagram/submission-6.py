class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}

        for char in s:
            h[char] = h.get(char, 0) + 1

        for char in t:
            if char in h:
                h[char] -= 1
            else:
                return False
            
        for char in t:
            if h[char] != 0:
                return False
        
        return True