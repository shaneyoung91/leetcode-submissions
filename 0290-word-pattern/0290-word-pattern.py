class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # create a hashmap (to store letter-word pairings)
        # split method on s to iterate through each word
        # create 2nd hashmap (this stores word-letter pairings)
        # loop through pattern and s.split() together at the same time using zip method
        # if letter not in the 1st hashmap, assign key-value as letter-word and vice versa for 2nd hashmap
            # inner if statement, if word in 2nd hashmap and 2nd hashmap index for word != letter, return False
        # else if letter not equal to the word in 1st hashmap, return False
        # exit the loop, return True
        
        letter_word_map = {}
        word_letter_map = {}
        words = s.split()
        
        # base case
        if len(pattern) != len(words):
            return False
        
        for letter, word in zip(pattern, words):
            if letter not in letter_word_map:
                if word in word_letter_map and word_letter_map[word] != letter:
                    return False
                letter_word_map[letter] = word
                word_letter_map[word] = letter
            elif letter_word_map[letter] != word:
                return False
            
        return True