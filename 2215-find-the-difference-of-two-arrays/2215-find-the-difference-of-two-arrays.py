class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        # append new arrays to answer 
        # iterate through num1 - if value is also in nums2, add value to new array
        # append updated array to answer
        # repeat for nums2 array
        
        answer = []
        dist_nums1 = []
        dist_nums2 = []
        
        for num in nums1:
            if num not in nums2:
                if num not in dist_nums1:
                    dist_nums1.append(num)
        
        answer.append(dist_nums1)
        
        for num in nums2:
            if num not in nums1:
                if num not in dist_nums2:
                    dist_nums2.append(num)  
        
        answer.append(dist_nums2)
        
        return answer