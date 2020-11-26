'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
'''

class Solution:
    def calculate(self, s: str) -> int:
        print(-3//2)
        if not s:
            return 0
        all_operators = ["+", "-", "*", "/"]
        all_digits = list(str(i) for i in range(10))
        curr_num = 0
        operator = '+'
        stack = []
        for idx, ch in enumerate(s):
            if ch in all_digits:
                curr_num = curr_num * 10 + int(ch)
            if ch in all_operators or idx == len(s) - 1 :
                if operator == '+':
                    stack.append(curr_num)
                elif operator == '-':
                    stack.append(-curr_num)
                elif operator == '*':
                    stack[-1] = stack[-1] * curr_num
                else:
                    stack[-1] = int(stack[-1] / curr_num)
                    
                curr_num = 0
                operator = ch
            
        return sum(stack)

