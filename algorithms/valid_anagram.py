#!/usr/local/bin/python

# Problem URL : https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = [0 for i in range(26)]
        
        for char in s:
            count[ord(char)-97] += 1
        for char in t:
            count[ord(char)-97] -= 1
            
        for val in count:
            if val != 0:
                return False
        return True