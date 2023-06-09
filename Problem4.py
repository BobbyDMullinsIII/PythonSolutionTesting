


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
        #Variables
        #Merge arrays, sort merged array, and store length in variable
        mergedArray = nums1 + nums2
        mergedArray.sort()
        arrayLength = len(mergedArray)
        oddLength = False
        
        #Makes oddLength variable true if array is calculated to be odd in length
        if arrayLength % 2 != 0:
            oddLength = True
           
        #Different calculations for odd or even length 
        if oddLength == True:
            #Calculation for odd length
            median = mergedArray[(arrayLength + 1) // 2 - 1]
        else:
            #Calculation for even length
            tempNum = mergedArray[arrayLength // 2 - 1] + mergedArray[arrayLength // 2]
            median = tempNum / 2.0
            
        return median