class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        new_list = []
        for i in nums:
            new_list.append(i)
        
        result = nums + new_list
        return result