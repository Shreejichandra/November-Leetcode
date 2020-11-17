'''
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.
'''

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        ans = 0 
        for i in range(1, n-1):
            if A[i-1] < A[i] > A[i+1]:
                left = right = i
                while left > 0 and A[left] > A[left-1]:
                    left -= 1
                while right + 1 < n and A[right] > A[right+1]:
                    right += 1
                ans = max(ans, (right-left+1))
        return ans
                
        
