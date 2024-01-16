class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        # create an empty array
        # iterate through candies array
        # check if current + extraCandies is greater than max candy in the array
        # return true if yes, false if no
        
        result = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        
        return result
        
        