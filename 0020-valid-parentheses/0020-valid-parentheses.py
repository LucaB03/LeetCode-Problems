class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in [')', '}', ']'] or s[len(s)-1] in ['(', '{', '[']:
            return False
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif stack.pop() + c not in ["()", "[]", "{}"]:
                return False
        return True if len(stack) == 0 else False