


from typing import List

class Problem11:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem11():
        #Main variables
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

        #Execute Solution
        #maxArea = Problem11.maxAreaBruteForce(height) #Brute force method
        maxArea = Problem11.maxAreaEfficient(height) #More efficient method

        #Solution printed out to console
        print(maxArea)
        
    def maxAreaBruteForce(height: List[int]) -> int:
        #Variables
        xVal = -1
        yVal = -1
        area = -1
        maxArea = 0
        
        #Compares each index to each other with two for loops (Can result in some duplicate calculations)
        for i in range (len(height)):
            for j in range (len(height)):
                #Will not calculate area with and index against itself
                if i != j:
                    xVal = abs(i - j)
                    yVal = min(height[i], height[j])
                    area = xVal * yVal
                    maxArea = max(maxArea, area)
                    
        #Returns final calculated max area
        return maxArea
    
    def maxAreaEfficient(height: List[int]) -> int:
        #Variables
        i = 0
        j = len(height) - 1
        area = -1
        maxArea = 0
        
        #Will not result in duplicate calculations, unlite brute force method
        while i < j:
            #Compares 'area' of current calculation with the 'maxArea' calculated so far
            area = min(height[i], height[j]) * (j - i)   
            maxArea = max(maxArea, area)   
            
            #Brings i and j closer if their current indexes are of differing heights
            if height[i] < height[j]:
                i += 1
            else:
                j-= 1
                
        #Returns final calculated max area
        return maxArea