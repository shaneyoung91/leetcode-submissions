class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #   Create counters for 's' and 't'
        #   Iterate through 't' counter's key-value pairs (items method)
        #   If value != 's' counter's value or letter not in 's' counter, return the key                   (letter)

        counter_s = Counter(s)
        counter_t = Counter(t)
        
        for letter, value in counter_t.items():
            if value != counter_s[letter] or letter not in counter_s:
                return letter
        

