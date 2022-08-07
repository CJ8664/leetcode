class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, n = 0, 0
        while i < len(arr):
            n += 1
            # If the arr element is not same as "n"
            # decrement "k" to indicate that one missing 
            # element is processed
            if n != arr[i]:
                k -= 1
            # If the element is the same as "n" just move
            # to the next element in array
            else:
                i += 1
            if k == 0:
                return n
        # If all "k" missing elements were not processed in array
        # n would be the last element in array + k remaining missing
        # elements to be processed
        return n + k
        