class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        # create a dictionary {}
        # iterate through array
        # assign counter to value of element
        # remove values where counter is > 1
        # return sum of values
        
        # ---- Alternative Solution -----
        # use Counter method
        # iterate through dictionary and sum key where value is <= 1
        
        count = Counter(nums)
        result = 0
        
        for key, value in count.items():
            if value <= 1:
                result += key
        
        return result