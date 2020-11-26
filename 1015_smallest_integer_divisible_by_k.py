'''
Given a positive integer K, you need to find the length of the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N. If there is no such N, return -1.

Note: N may not fit in a 64-bit signed integer.
'''

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        not_possible = [0, 2, 4, 5, 6, 8]
        unit_place = K % 10
        if unit_place in not_possible:
            return -1
        
        num = 1
        length = 1
        while num % K != 0:
            num = num * 10 + 1
            length += 1
      
        return length
        
