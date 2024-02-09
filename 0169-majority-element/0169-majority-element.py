class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # create hashmap using Counter method
        # iterate through hashmap, access key-value pairs using items method
        # if value > length of nums array // 2, return key
        
        hashmap = Counter(nums)
        
        for key, value in hashmap.items():
            if value > len(nums) // 2:
                return key
        
        