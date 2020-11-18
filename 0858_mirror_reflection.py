'''
There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)
'''


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        extension = q
        reflection = p
        # extension * p = reflection * q
        while (extension % 2 == 0 and reflection % 2 == 0):
            extension //= 2
            reflection //= 2
        
        if extension % 2 != 0 and reflection % 2 != 0:
            return 1
        if extension % 2 == 0 and reflection % 2 != 0:
            return 0
        if extension % 2 != 0 and reflection % 2 == 0:
            return 2
        
