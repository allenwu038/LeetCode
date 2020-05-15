# Python3
# runtime: faster than 91.83% of submissions
# memory: less than 5.71% of submissions

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # create sorted list from nums1 and nums2
        masterList = sorted(nums1 + nums2)
        
        # if list has odd number of elements, return middle number
        if len(masterList)%2:
            return masterList[len(masterList)//2]
        
        #if list length is even, average two middle numbers
        else:
            return (masterList[len(masterList)//2] + mergedList[len(masterList)//2 - 1])/2
            
        
