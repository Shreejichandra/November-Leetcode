'''
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character 
in this substring is greater than or equal to k.
'''

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or n < k:
            return 0
        elif k <= 1:
            return n
        
        frequency = Counter(s)
        
        l = 0
        while l < n and frequency[s[l]] >= k:
            l += 1
        if l == n:
            return n
        part1 = self.longestSubstring(s[0:l], k)
        while l < n and frequency[s[l]] < k:
            l += 1
        if l < n:
            part2 = self.longestSubstring(s[l:], k)
        else:
            part2 = 0
        return max(part1, part2)
        
        
