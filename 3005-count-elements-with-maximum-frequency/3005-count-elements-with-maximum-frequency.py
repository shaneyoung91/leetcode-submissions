class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        # create hashmap using Counter method
        # create array using hashmap values
        # create variable for max count in array
        # create variable for result
        # iterate through array, if element == max count, add element to result variable
        # return result
        
        hashmap = Counter(nums)
        list_map = list(hashmap.values())
        max_count = max(list_map)
        
        result = 0
        
        for i in list_map:
            if i == max_count:
                result += i
        
        return result