#!/usr/local/bin/python

# Problem URL : https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        alp_count = [0 for i in range(26)]
        
        for char in s:
            alp_count[ord(char)-97] +=1
            
        print(alp_count)
        
        i = 0
        while i < len(s):
            if alp_count[ord(s[i])-97] == 1:
                return i
            i +=1
        return -1