'''
Question

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def find_right(parent_node, left_node, right_node):
            if left_node == None:
                return
            else:
                left_node.next = right_node
                if parent_node.next == None:
                    right_node.next = None
                else:
                    right_node.next = parent_node.next.left

                find_right(parent_node.left, parent_node.left.left, parent_node.left.right)
                find_right(parent_node.right, parent_node.right.left, parent_node.right.right)
        
        if root and root.left:
            find_right(root, root.left, root.right)
        
        
        return root
        
