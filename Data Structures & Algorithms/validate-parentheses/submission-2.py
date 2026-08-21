
class Solution:
    def isValid(self, s: str) -> bool:
        d = {"}": "{", ")": "(", "]": "["}
        stack = []

        for ch in s:
            if len(stack) > 0 and ch in {"}", "]", ")"} and d[ch] == stack[-1]:
                stack.pop()
            else: 
                stack.append(ch)
                
        return len(stack) == 0

