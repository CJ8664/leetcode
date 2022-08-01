class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) 
        stack = collections.deque()
        for r in range(len(temperatures)):
            # If the current temperature is greater than top of stack
            # means we found result for top of stack. Update the result
            # for the poped element. Keep checking with new top until 
            # the stack is empty or stack top is greater than current
            while stack and temperatures[r] > stack[-1][0]:
                _, l = stack.pop()
                result[l] = r - l
                
            # Stack is empty or stack top is greater than current,
            # this means we now put this temperatur as "pending" in stack
            stack.append((temperatures[r], r))
        return result
                    
            
                
        
        
        