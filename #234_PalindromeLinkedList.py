# 234. Palindrome Linked List (Easy)
# https://leetcode.com/problems/palindrome-linked-list/
# https://www.youtube.com/watch?v=wk4QsvwQwdQ&list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-&index=6


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # O(N) time, O(1) space
    def isPalindrome(self, head):
        if head is None:
            return True
        
        slow, fast = head, head
        stack = []
        
        # move fast to the end and slow to the middle
        while fast and fast.next:  # O(N) time, O(1) space
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
        
        while (slow and len(stack)): # O(N) time, O(1) space
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        return True