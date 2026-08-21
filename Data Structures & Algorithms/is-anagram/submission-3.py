class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        for char in s:
            
            if char in h1:
                h1[char] += 1
            else:
                h1[char] = 1

        for char in t:
            if char in h1:
                h1[char] -= 1
            else:
                return False
            
        for char in s:
            if h1[char] != 0:
                return False
            
        return True