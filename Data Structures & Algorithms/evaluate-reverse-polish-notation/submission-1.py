class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operands=['+','-','*','/']
        for i in range(0,len(tokens)):
            if tokens[i] not in operands:
                stack.append(int(tokens[i]))
            
            else:
                operand2=stack.pop()
                operand1=stack.pop()

                if tokens[i]=='+':
                    stack.append(operand1+operand2)
                elif tokens[i] == "-":
                    stack.append(operand1 - operand2)
                elif tokens[i] == "*":
                    stack.append(operand1 * operand2)
                elif tokens[i] == "/":
                    stack.append(int(operand1 / operand2))
        return stack[0]

        