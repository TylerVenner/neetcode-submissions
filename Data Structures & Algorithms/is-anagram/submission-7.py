class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = {}, {}

        if len(s) != len(t):
            return False;
        
        for char in s:
            if char in a:
                a[char] += 1
            else:
                a[char] = a.get(char, 0) + 1
         
        for char in t:
            if char in b:
                b[char] += 1
            else:
                b[char] = b.get(char, 0) + 1

        return a == b
 