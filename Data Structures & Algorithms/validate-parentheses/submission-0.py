class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        l = []
        for c in s:
            l.append(c)

        while len(l) != 0:
            curr = l.pop(0)
            
            if curr in ["}", "]", ")"] and len(stack) == 0:
                return False
            
            if curr in ["{", "[", "("]:
                stack.append(curr)

            if curr == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(curr)

            if curr == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(curr)

            if curr == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(curr)

        return len(stack) == 0

            



    