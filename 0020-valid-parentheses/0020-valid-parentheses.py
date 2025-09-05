class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # for char in s:
        #     if char == '(' or char == '{' or char == '[':
        #         stack.append(char)
        #     else:
        #         if not stack:
        #             return False
        #         top = stack.pop()

        #         if char == ')' and top != '(':
        #             return False
        #         if char == '}' and top != '{':
        #             return False
        #         if char == ']' and top != '[':
        #             return False
        # return not stack
        stack = []
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)
        return True if not stack else False