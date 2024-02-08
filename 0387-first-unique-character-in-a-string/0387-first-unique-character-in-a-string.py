class Solution:
    def firstUniqChar(self, s: str) -> int:
        # create Counter
        # iterate through Counter key-value pairs (items method)
        # if letter's value is == 1, return the return the index of string linked to letter
        # outside the loop return -1
        
        counter_s = Counter(s)
               
        for i, n in counter_s.items():
            if n == 1:
                return s.index(i)
        
        return -1
        

        
        
        