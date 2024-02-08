class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
       # for linear runtime and constant space complexity:
       # find the sum of the hashset
       # return 2 * hashset less sum of list
    
        hashset_sum = sum(set(nums))

        return ((2 * hashset_sum) - sum(nums))