'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        temp = None
        carry = 0
        while len(stack1) or len(stack2) or carry:
            add = 0
            if len(stack1):
                add += stack1[-1]
                stack1.pop()
            if len(stack2):
                add += stack2[-1]
                stack2.pop()
            add += carry
            node = ListNode(add%10)
            carry = add//10
            node.next = temp
            temp = node
        return temp
        
