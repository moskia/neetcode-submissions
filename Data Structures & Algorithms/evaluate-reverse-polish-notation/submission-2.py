class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens: 
            if c == '+':
                elt1 = stack.pop()
                elt2 = stack.pop()
                stack.append(elt2 + elt1)
            elif c == '*':
                elt1 = stack.pop()
                elt2 = stack.pop()
                stack.append(elt2 * elt1)
            elif c == '/':
                elt1 = stack.pop()
                elt2 = stack.pop()
                stack.append(int(elt2 / elt1))
            elif c == '-':
                elt1 = stack.pop()
                elt2 = stack.pop()
                stack.append(elt2 - elt1)
            else:
                stack.append(int(c))
        
        return stack.pop()