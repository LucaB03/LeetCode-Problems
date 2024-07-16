class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif stack.pop() + c not in ["()", "[]", "{}"]:
                return False
        return True if len(stack) == 0 else False