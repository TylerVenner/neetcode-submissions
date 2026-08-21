class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 0:
            return True
        
        stack = []
        i = 0

        while i < len(s):
            new = s[i]
            i += 1

            if new == "}":
                if len(stack) == 0:
                    return False
                
                if stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(new)
            elif new == "]":
                if len(stack) == 0:
                    return False
                
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(new)
            elif new == ")":
                if len(stack) == 0:
                    return False
                
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(new)
            else:
                stack.append(new)


        return len(stack) == 0