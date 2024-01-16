class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        # iterate through the array and assign value (1 or -1)
        # return the sum of new variable
        
        result = 0
        
        for i in operations:
            if i == "++X" or i == "X++":
                result += 1
            else:
                result -= 1
        
        return result