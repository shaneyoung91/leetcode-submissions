class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create hashmap using Counter on nums array
        # key == number
        # value == count
        # create new array
        # sort the hashmap items in desc order, set key to count using itemgetter()
        # iterate through 'k' using range()
        # append the key from the sorted hashmap to new array (use double square notation to access key in the sub-tuple)
        # return new array
        
        hashmap = Counter(nums)
        sorted_map = sorted(hashmap.items(), key=itemgetter(1), reverse=True)
        result = []
        
        for i in range(k):
            result.append(sorted_map[i][0])
            
        return result