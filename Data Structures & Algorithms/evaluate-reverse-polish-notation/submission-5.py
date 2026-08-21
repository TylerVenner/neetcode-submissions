class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left) + int(right))
            elif ch == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left) - int(right))
            elif ch == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left) * int(right))
            elif ch == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
            else:
                stack.append(int(ch))

        return stack[0]
 