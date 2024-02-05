class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        # create sets for nums1 and nums2
        # assign variable for the difference in set_nums1 and set_nums2
            # convert to a list
        # repeat for difference in set_nums2 and set_nums1
        # return both variables as subarrays
        
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        
        dist_nums1 = list(set_nums1 - set_nums2)
        dist_nums2 = list(set_nums2 - set_nums1)
        
        return [dist_nums1, dist_nums2]