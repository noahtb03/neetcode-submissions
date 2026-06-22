class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in matches:  # char is a closing bracket
                if not stack or stack[-1] != matches[char]:
                    return False
                stack.pop()
            else:  # char is an opening bracket
                stack.append(char)

        return len(stack) == 0

        