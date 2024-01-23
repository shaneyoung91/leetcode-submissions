class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        new_dict = {}
        
        for index, num in enumerate(nums):
            if num in new_dict and abs(index - new_dict[num]) <= k:
                return True
            new_dict[num] = index
        
        return False