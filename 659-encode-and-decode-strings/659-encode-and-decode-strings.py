class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        result = []
        for s in strs:
            result.extend([str(len(s)), "#", s])
        return "".join(result)


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        result = []
        # write your code here
        i = 0
        while i < len(str):
            l_str = ""
            while str[i] != "#":
                l_str += str[i]
                i += 1
            l_str = int(l_str)
            result.append(str[i + 1: i + 1 + l_str])
            i = i + 1 + l_str
        return result
