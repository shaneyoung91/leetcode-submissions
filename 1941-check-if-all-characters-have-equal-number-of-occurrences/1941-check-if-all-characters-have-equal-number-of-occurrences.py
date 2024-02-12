class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        # create hashmap using Counter method
        # create a hashset based on hashmap values
        # if the length of the hashset == 1, return True (as all occurences are same amount)
        # else return False (if hashset length is > 1 due to different occurences of each letter)
        
        hashmap = Counter(s)
        hashset = set(hashmap.values())
        
        if len(hashset) == 1:
            return True
        else:
            return False
        
        