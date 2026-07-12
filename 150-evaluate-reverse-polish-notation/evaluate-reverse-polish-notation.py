class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        hashh = {'+','-','*','/'}
        
        for i in tokens:
            output = None
            if i in hashh:
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()

                    if i == '+':
                        output = a + b
                        stack.append(output)
                    elif i == '-':
                        output = a - b
                        stack.append(output)
                    elif i == '*':
                        output = a * b
                        stack.append(output)
                    elif i == '/':
                        output = a // b if a * b > 0 else -(-a//b)
                        stack.append(output)
            else:
                stack.append(int(i))

        return stack[0]