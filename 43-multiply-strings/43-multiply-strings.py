class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        short, long = (num1, num2) if len(num1) < len(num2) else (num2, num1)
        result = [0 for _ in range(len(long) * 2)]
        i, j, c = 0, 0, 0
        for s in short[::-1]:
            j = i
            for l in long[::-1]:
                t = int(s) * int(l) + c
                result[j], c, j = result[j] + t % 10, t // 10, j + 1
            if c > 0:
                result[j] += c
            i, j, c = i + 1, 0, 0
        if c > 0:
            result[i] += c
        c = 0
        for i, x in enumerate(result):
            result[i] = (x + c) % 10
            c = (x + c) // 10 
        while result[-1] == 0:
            result.pop()
        return "".join([str(x) for x in result[::-1]])
                
                
                
                
        