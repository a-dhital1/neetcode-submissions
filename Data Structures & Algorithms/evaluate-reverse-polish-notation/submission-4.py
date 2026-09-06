class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:
            if i == '+':
                back_one = stack.pop()
                back_two = stack.pop()
                stack.append(back_two + back_one)
            elif i == '-':
                back_one = stack.pop()
                back_two = stack.pop()
                stack.append(back_two - back_one)
            elif i == '*':
                back_one = stack.pop()
                back_two = stack.pop()
                stack.append(back_two * back_one)
            elif i == '/':
                back_one = stack.pop()
                back_two = stack.pop()
                stack.append(int(back_two / back_one))
            else:
                stack.append(int(i))

        return stack[0]