'''
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.
'''

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums = sorted(nums)
        l, r = 1, nums[-1]
        
        while l <= r:
            mid = (l+r)//2
            total = 0
            for i in nums:
                total += ceil(i/mid)
            if total > threshold:
                l = mid+1
            else:
                ans = mid
                r = mid-1
       
        return ans
       
                
                
        
