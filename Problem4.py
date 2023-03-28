

from typing import List

class Problem4:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem4():
        #Main variables
        nums1 = [1, 3]
        nums2 = [2]

        #Execute solution
        median = Problem4.findMedianSortedArrays(nums1, nums2)

        #Solution printed out to console
        print(median)
        
    
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        
        oddLength = False
        
        mergedArray = nums1 + nums2
        mergedArray.sort()
        arrayLength = len(mergedArray)
        
        if arrayLength % 2 != 0:
            oddLength = True
            
        if oddLength == True:
            median = mergedArray[(arrayLength + 1) // 2 - 1]
        else:
            tempNum = mergedArray[arrayLength // 2 - 1] + mergedArray[arrayLength // 2]
            median = tempNum / 2.0
            
        return median