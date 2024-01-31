class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashset = set(sentence)
        
        return len(hashset) == 26