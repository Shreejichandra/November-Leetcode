'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
'''

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        stack = [start]
        visited = [0] * len(arr)
        visited[start] = 1
        while stack:
            main = stack.pop()
            left = main - arr[main]
            right = main + arr[main]
            if 0 <= left < len(arr) and visited[left] == False:
                if arr[left] == 0:
                    return True
                else:
                    stack.append(left)
                    visited[left] = True
            if 0 <= right < len(arr) and visited[right] == False:
                if arr[right] == 0:
                    return True
                else:
                    stack.append(right)
                    visited[right] = True
        return False
        
