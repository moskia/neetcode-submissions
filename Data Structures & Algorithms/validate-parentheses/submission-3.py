class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '[' :
                stack.append(']')
            elif c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != c:
                    return False

        if stack:
            return False
        return True