class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/':
                stack.append(int(i))
            elif i == '+':
                cur_num = stack.pop()
                prev_num = stack.pop()
                stack.append(prev_num + cur_num)
            elif i == '-':
                cur_num = stack.pop()
                prev_num = stack.pop()
                stack.append(prev_num - cur_num)
            elif i == '*':
                cur_num = stack.pop()
                prev_num = stack.pop()
                stack.append(prev_num * cur_num)
            elif i == '/':
                cur_num = stack.pop()
                prev_num = stack.pop()
                stack.append(int(prev_num / cur_num))

        return stack.pop()