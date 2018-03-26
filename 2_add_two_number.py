# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = ListNode(0)
        currentRoot = result
        while l1 != None or l2 != None:
            if(l1 != None):
                currentRoot.val += l1.val
                l1 = l1.next
            if(l2 != None):
                currentRoot.val += l2.val
                l2 = l2.next
            if currentRoot.val >= 10:
                currentRoot.val %= 10
                currentRoot.next = ListNode(1)
            elif l1 != None or l2 != None:
                currentRoot.next = ListNode(0)
            currentRoot = currentRoot.next
            
        return result