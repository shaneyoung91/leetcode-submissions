class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        # create a hashmap
        # key == row
        # value == characters assigned to that row
        # iterate through words array
        # lowercase word
        # inner for loop iterates through hashmap values
        # if hashset of lowercase word is subset of hashmap value, append to new array
        # exit the loop, return new array
        
        hashmap = {
            "1" : "qwertyuiop",
            "2" : "asdfghjkl",
            "3" : "zxcvbnm"
        }
        
        result = []
        
        for word in words:
            lower_word = word.lower()
            
            for char in list(hashmap.values()):
                if set(lower_word).issubset(char):
                    result.append(word)
                    
        return result
            
        

            