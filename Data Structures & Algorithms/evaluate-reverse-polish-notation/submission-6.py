class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        stack = []
        for i in range(len(tokens)):

            res = 0
            if tokens[i] == '+':
                res = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
                continue
            
            elif tokens[i] == '-':
                res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
                continue

            
            elif tokens[i] == '*':
                res = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
                continue

            
            elif tokens[i] == '/':
                res = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
                continue

            
            stack.append(int(tokens[i]))
        return stack[-1]