```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        pre_req_map = defaultdict(list)
        
        def check_prereq(c):
            # This course has no pre-req
            if not pre_req_map[c]:
                return True
            # Pre-req cycle
            if c in visiting: 
                return False

            # Mark course as visiting
            visiting.add(c)
            
            # Check all the pre-req of current course
            for p in pre_req_map[c]:
                if not check_prereq(p):
                    return False                
            
            # Remove current course as visiting so that other 
            # courses can check it in their search
            visiting.remove(c)
            
            # Empty the pre-req for this course indicating that
            # It can be taken. This saves memory and avoids the need 
            # for additional tracker
            pre_req_map[c] = []
            
            return True
        
        for c, p in prerequisites:
            pre_req_map[c].append(p)
            
        for c in range(numCourses):
            if not check_prereq(c):
                return False
        return True
        
```
