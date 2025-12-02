class Solution(object):
    def isValid(self, s):
        stack = []

        # correct bracket mapping
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in pairs.values():   # opening brackets
                stack.append(ch)
            else:                      # closing brackets
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        
        return len(stack) == 0