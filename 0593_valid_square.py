'''
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.
''''

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def distance(x, y):
            return (x[0]-y[0])**2 + (x[1]-y[1])**2
        
        all_dist = [distance(p1, p2), distance(p1, p3), distance(p1, p4), 
                    distance(p2, p3), distance(p2, p4), distance(p3, p4)]
        
        unique_dist = set(all_dist)               
        if len(unique_dist) == 2: 
            if 0 not in unique_dist:
                return True
        return False
        
