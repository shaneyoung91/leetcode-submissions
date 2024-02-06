class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        hashmap = {}
        
        for i in range(len(names)):
            hashmap[heights[i]] = names[i]
        
        sort_heights = sorted(heights, reverse=True)
        
        result = []
        
        for height in sort_heights:
            result.append(hashmap[height])
    
        return result

        