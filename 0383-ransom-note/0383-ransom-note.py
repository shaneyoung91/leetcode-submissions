class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count_note = Counter(ransomNote)
        count_mag = Counter(magazine)
        
        for char, count in count_note.items():
            if count > count_mag[char]:
                return False
        
        return True
            

           