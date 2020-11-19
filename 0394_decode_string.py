'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
'''

class Solution:
    def decodeString(self, s: str) -> str:
        "abc3[cd]xyz"
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                temp = ""
                while (stack[-1] != "["):
                    temp += stack.pop()
                stack.pop()
                n = ""
                while (stack and stack[-1].isdigit()):
                    n += stack.pop()
                decoded = int(n[::-1]) * temp[::-1]
                for j in decoded:
                    stack.append(j)
        ans = "".join(ch for ch in stack)
        return ans
                    
            
