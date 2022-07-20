class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while i >= 0:
            t = digits[i] + carry
            digits[i], carry = t % 10, t // 10
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits
        