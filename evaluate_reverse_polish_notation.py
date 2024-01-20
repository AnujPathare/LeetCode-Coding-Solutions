# import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        operands = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                if token == '+':
                    result = operands[-2] + operands[-1]
                elif token == '-':
                    result = operands[-2] - operands[-1]
                elif token == '*':
                    result = operands[-2] * operands[-1]
                elif token == '/':
                    # result = math.trunc(operands[-2] / operands[-1])
                    result = int(float(operands[-2])/operands[-1])

                operands.pop()
                operands.pop()
                operands.append(result)
            else:
                operands.append(int(token))
        
        return operands.pop()
    

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

obj = Solution()
print(obj.evalRPN(tokens))