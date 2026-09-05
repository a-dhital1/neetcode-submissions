class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' or i == '}' or i == ']':
                if len(stack) != 0:
                    top = stack.pop()
                else:
                    return False

                if i == ')' and top != '(':
                    return False
                if i == '}' and top != '{':
                    return False
                if i == ']' and top != '[':
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
        
        