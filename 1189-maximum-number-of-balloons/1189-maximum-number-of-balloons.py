class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        # create 2 hashmaps using Counter on string 'balloon' and parameter 'text'
        # create count variable, set to infinity using float('inf')
        # iterate over key, value using balloon.items()
        # if value == 0, return 0 (meaning no character in balloon is not in hashmap)
        # set count variable to minimum of either existing count or 
            # the current key in hashmap text divided by value (required # in the word 'balloon')
        # exit the loop, return the count
        
        count = float('inf')
        
        balloon = Counter('balloon')
        hashmap = Counter(text)
        
        for key, value in balloon.items():
            if value == 0:
                return 0
            count = min(count, hashmap[key] // value)
                
        return count