


from typing import List

class Problem1:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem1():
        #Main variables
        nums = [2, 7, 11, 15]
        target = 9
        
        #Execute solution
        #returnArray = Problem1.twoSumBruteForce(nums, target)
        returnArray = Problem1.twoSumEfficient(nums, target)
        
        #Solution printed out to console
        print(returnArray)
    
    
    def twoSumBruteForce(nums: List[int], target: int) -> List[int]:  
        #Double for loop to iterate through each value and compare to every other value
        #(will result in comparisons with the same indices duplicating a few times)   
        for i in range(len(nums)):
            for j in range(len(nums)):
                #Do not compare if same index
                if i != j:
                    #Check if equal to target
                    if (nums[i] + nums[j]) == target:
                        #Returns indices if two separate indices to equal target are found
                        return [i, j]
                   
        #Will only return this if two separate indices equaling target are not found
        return List[0, 0]
    
    
    def twoSumEfficient(nums: List[int], target: int) -> List[int]:
        tempDict = {}
        
        #Loop through array only one time using dictionary
        for i in range(len(nums)):
            
            indiceOneVal = nums[i]
            indiceTwoVal = target - indiceOneVal
            
            #Check if equal to target
            if indiceTwoVal in tempDict:   
                #returns indices if two separate indices to equal target are found 
                index = tempDict[indiceTwoVal]
                return [index, i]
            
            tempDict[indiceOneVal] = i
                  
        #Will only return this if two separate indices equaling target are not found
        return List[0, 0]