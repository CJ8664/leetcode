```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get count of each number
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # Create a dict freq -> all the numbers with that freq
        freq = {}
        for n, f in count.items():
            if f not in freq:
                freq[f] = []
            freq[f].append(n)

        res = []
        for f in range(len(nums), 0, -1):
            # get all the numbers for the freq starting with highest
            if f in freq:
                for n in freq[f]:
                    res.append(n)
                    if len(res) == k:
                        return res

```
