class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # create a hashmap with each number as key and frequency as value
        # add frequency to counter each time number appears again in the hashmap
        hashMap = {}
        count = 0
        
        for num in nums:
            if num in hashMap:
                count += hashMap[num]
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        return count
                
        
            