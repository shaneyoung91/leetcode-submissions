class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        count = 0
        words = text.split()
        
        for word in words:
            valid = True
            
            for letter in word:
                if letter in brokenLetters:
                    valid = False
                    break
            
            if valid:
                count += 1
            
        return count