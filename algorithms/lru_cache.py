#!/usr/local/bin/python

# Problem URL : https://leetcode.com/problems/lru-cache/description/

class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.data_dict = dict()
        self.lru_list = list()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        data = self.data_dict.get(key, -1)
        
        # Element does exist
        if data != -1 :
        
            # Update the lru_list
            # If the key is in lru list remove it and append it to the last position
            if key in self.lru_list:
                self.lru_list.remove(key)
            self.lru_list.append(key)

        return data

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # Check if the cache is full
        
        # New element need to remove the oldest element first
        if key not in self.lru_list and len(self.lru_list) == self.capacity: 
            
            rm_key = self.lru_list[0] # ele at 0 is the oldest element
            del self.lru_list[0] # Remove the element from thw list
            del self.data_dict[rm_key] # Remove the element from the dict
            
        self.data_dict[key] = value
        if key in self.lru_list:
            self.lru_list.remove(key)
        self.lru_list.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)