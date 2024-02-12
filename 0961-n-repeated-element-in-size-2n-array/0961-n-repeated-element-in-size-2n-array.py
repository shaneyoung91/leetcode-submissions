class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        # create hashmap using Counter method
        
        # create new variable to determine 'n'
            #   n = nums.length / 2
            #   unique_ele = n + 1
        
        # iterate through the hashmap num-count pairs using items method
        # if count == n, return num
        
        hashmap = Counter(nums)
        n = len(nums) / 2
        
        for num, count in hashmap.items():
            if count == n:
                return num