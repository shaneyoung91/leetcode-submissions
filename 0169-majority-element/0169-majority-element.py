class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort the nums array
        # since majority element appears more than [length of array / 2] times, we can access the value with this formula
        # return the value of the sorted nums array based on the index position of [length of array / 2]
        
        sorted_nums = sorted(nums, reverse=True)
        
        return sorted_nums[(int(len(sorted_nums) / 2))]
        
        