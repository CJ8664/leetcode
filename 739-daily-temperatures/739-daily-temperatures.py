class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        idx = len(temperatures) - 2
        while idx >= 0:
            if temperatures[idx] < temperatures[idx + 1]:
                answer[idx] = 1
            else:
                i = idx + answer[idx + 1] + 1
                while i < len(temperatures):
                    if temperatures[i] > temperatures[idx]:
                        answer[idx] = i - idx
                        break
                    elif answer[i] == 0:
                        answer[idx] = 0
                        break
                    else:
                        i = i + answer[i]
            idx -= 1
        return answer
                    
                    
            
                
        
        
        