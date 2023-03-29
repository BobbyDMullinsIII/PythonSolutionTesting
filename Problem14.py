


from typing import List

class Problem14:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem14():
        #Main variables
        strs = ["flower", "flow", "flight"]

        #Execute Solution
        commonPrefix = Problem14.longestCommonPrefix(strs)

        #Solution printed out to console
        print(commonPrefix)
        
    def longestCommonPrefix(strs: List[int]) -> str:
        i = 0 #Counting variable for while loop
        
        #Sort array and find the smallest length from beginning and end strings
        strs.sort()
        end = min(len(strs[0]), len(strs[len(strs) - 1]))
        
        #Count until 'i' is at location of end of common prefix between all strings
        while i < end and strs[0][i] == strs[len(strs) - 1][i]:
            i += 1
        
        #Return calculated common prefix
        return strs[0][:i]
        