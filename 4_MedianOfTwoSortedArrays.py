# Python3
# runtime: faster than 91.83% of submissions
# memory: less than 5.71% of submissions

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = sorted(nums1 + nums2)
        
        if len(mergedList)%2:
            return mergedList[len(mergedList)//2]
        else:
            return (mergedList[len(mergedList)//2] + mergedList[len(mergedList)//2 - 1])/2
            
        
