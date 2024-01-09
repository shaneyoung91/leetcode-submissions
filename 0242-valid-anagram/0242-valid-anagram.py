class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # base case
        if len(s) != len(t):
            return False
        
        # split and sort both strings
        # iterate and compare characters in each string
        sort_s = sorted(s)
        sort_t = sorted(t)
        
        for i in range(len(sort_s)):
            if sort_s[i] != sort_t[i]:
                return False
        
        return True
                
        