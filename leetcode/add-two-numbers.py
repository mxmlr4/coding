# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = tail = ListNode(-1)
        digit = 0
        n1, n2 = l1, l2
        while n1 or n2:
            val = (n1.val if n1 else 0) + (n2.val if n2 else 0) + digit
            tail.next = ListNode(val % 10)
            digit = val // 10

            tail = tail.next
            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None

        if digit:
            tail.next = ListNode(digit)

        return result.next
    
    