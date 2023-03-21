


from typing import List


class Problem1:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem1(self):
        #Main variables
        nums = List[2, 7, 11, 15]
        target = 9
        
        #Execute solution
        returnArray = Problem1.twoSumBruteForce(nums, target)
        
        #Solution printed out to console
        print(returnArray)
    
    @staticmethod
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:     
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if (nums[i] + nums[j]) == target:
                        return [i, j]
                   
        #Will only return this if two separate indices equaling target are not found
        return List[0, 0]
    
    @staticmethod 
    def twoSumEfficient(self, nums: List[int], target: int) -> List[int]:
        tempDict = {}
        
        for i in range(len(nums)):
            
            indiceOneVal = nums[i]
            indiceTwoVal = target - indiceOneVal
            
            if indiceTwoVal in tempDict:    
                index = tempDict[indiceTwoVal]
                return [index, i]
            
            tempDict[indiceOneVal] = i
                  
        #Will only return this if two separate indices equaling target are not found
        return List[0, 0]