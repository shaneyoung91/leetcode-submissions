class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashmap = {}
        
        for letter in s:
            if letter not in hashmap:
                hashmap[letter] = 1
            else:
                hashmap[letter] += 1
            
            if hashmap[letter] >= 2:
                return letter

            