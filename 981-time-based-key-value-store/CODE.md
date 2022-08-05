```python
class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        vals = self.data[key]

        # IF the timestamp is greater than the maximum 
        # recorded ts than return the last ts
        if timestamp > vals[-1][1]:
            return vals[-1][0]
        
        l, r = 0, len(vals) - 1
        while l <= r:
            mid = (l + r) // 2
            if vals[mid][1] == timestamp:
                return vals[mid][0]
            
            if timestamp > vals[mid][1]:
                l = mid + 1
            else:
                r = mid - 1
            print(l, r, mid, timestamp)
            
        # l is the index where you would have inserted new 
        # timestamp hence the maximum ts less than it is at l-1
        return vals[l-1][0] if l > 0 else ""
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```
