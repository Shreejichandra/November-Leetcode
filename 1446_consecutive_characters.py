'''Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.
'''

class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        ans = 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                count += 1
            else:
                ans = max(count, ans)
                count = 1
        ans  = max(count, ans)
        return ans
