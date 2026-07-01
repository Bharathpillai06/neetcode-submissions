class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        x = {'(':')','{':'}', '[':']'}
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in x:
                stack.append(char)
            else:
                if not stack:
                    return False
                if x[stack.pop()] != char:
                    return False

        return not stack

     