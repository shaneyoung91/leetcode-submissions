class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        hashmap = {}
        
        for num in arr:
            hashmap[num] = hashmap.get(num, 1) + 1

        unique = set(hashmap.values())
        
        if len(unique) == len(hashmap):
            return True
        else:
            return False
