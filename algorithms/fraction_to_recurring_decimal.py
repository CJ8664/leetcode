#!/usr/local/bin/python

# Problem URL https://leetcode.com/problems/fraction-to-recurring-decimal/description/

class Solution(object):
    
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        pause_append = False
        fr_str = ''
        partial_fr = ''
        fq = 0
        
        for i in xrange(10):
            quotient = numerator/denominator
            remainder = numerator - quotient*denominator
            numerator = remainder * 10
            
            if i == 0 :
                fq = quotient
            
            if(str(quotient) not in fr_str):
                if (quotient == 0 and i == 0 ):
                    continue
                fr_str = fr_str + partial_fr + str(quotient)
                partial_append = False
                partial_fr = ''
            else:
                fr_idx = fr_str.find(str(quotient))
                fq = str(fq) + '.' + fr_str[:fr_idx]
                fr_str = fr_str[fr_idx : ]
                pause_append = True
            
            if pause_append:
                partial_fr += str(quotient)
            
            print quotient, remainder , numerator
            
            if ( fr_str == partial_fr):
                return str(fq) + '(' + fr_str + ')'
                break
            elif ( remainder == 0 ) :
                if (fr_str != '0'):
                    return str(fq) + '.' + fr_str 
                else:
                    return str(fq)
                break
                
        print fq, fr_str 
      
