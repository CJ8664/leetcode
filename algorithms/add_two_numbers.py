#!/usr/local/bin/python

# Problem URL : https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        
        solution_list = None
        start_node = None
        
        while (True):
            temp_sum = l1.val + l2.val + carry
            units_val = temp_sum%10
            carry = temp_sum/10
            
            temp_node = ListNode(units_val)
            
            if (solution_list is None): # First answer
                solution_list = temp_node
                start_node = temp_node
            else:
                solution_list.next = temp_node
                solution_list = solution_list.next
                
            x = start_node
            """
            while (True):
                print(x.val)
                x = x.next
                if x is None:
                    break
            """
                
            l1 = l1.next
            l2 = l2.next
            
            if l1 is None or l2 is None:
                break
            
        if(l1 is None and l2 is not None):
            # Iterate over remaining l2 node 
            while(True):
                temp_sum = l2.val + carry
                units_val = temp_sum%10
                carry = temp_sum/10
            
                temp_node = ListNode(units_val)
                solution_list.next = temp_node
                solution_list = solution_list.next
                l2 = l2.next
                
                if l2 is None:
                    break
                
        elif(l2 is None and l1 is not None):
            # Iterate over remaining l1 node 
            while(True):
                temp_sum = l1.val + carry
                units_val = temp_sum%10
                carry = temp_sum/10
            
                temp_node = ListNode(units_val)
                solution_list.next = temp_node
                solution_list = solution_list.next
                l1 = l1.next
                
                if l1 is None:
                    break
                    
        if carry != 0:
            temp_node = ListNode(carry)
            solution_list.next = temp_node
            solution_list = solution_list.next
                
        return start_node
