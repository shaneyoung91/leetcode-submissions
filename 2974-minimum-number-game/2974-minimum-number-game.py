class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        # create a new array
        # iterate through the array
        # remove 2 minimum elements, then add the largest of the two to the new array first
        
        result = []

        while len(nums) > 1:
            alice_choice = min(nums)
            nums.remove(alice_choice)
            
            bob_choice = min(nums)
            nums.remove(bob_choice)
            
            result.append(bob_choice)
            result.append(alice_choice)
        
        return result