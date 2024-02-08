class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # create a hashmap using Counter
        # iterate through hashmap key-value
        # if value == 1, return number
        
        hashmap = Counter(nums)
        
        for num, value in hashmap.items():
            if value == 1:
                return num