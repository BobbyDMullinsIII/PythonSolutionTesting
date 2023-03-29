


class Problem3:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem3():
        #Main variables
        s = "abcabcbb"

        #Execute solution
        substringLength = Problem3.lengthOfLongestSubstring(s)

        #Solution printed out to console
        print(substringLength)
    
    
    def lengthOfLongestSubstring(s: str) -> int:
        #Variables
        checkStr = ""
        substringLength = -1
        
        #If string 's' is null or empty or has a length of 0, return 0
        if len(s.strip()) == 0 or len(s) == 0:
            return 0
        
        #If string 's' has a length of 1, return 1
        if len(s) == 0:
            return 1
        
        #Go through each character in string 's'
        for i in range(len(s)):
            #If a repeating character is found, reset checkStr
            if s[i] in checkStr:
                try:
                    checkStr = checkStr[checkStr.index(s[i]) + 1]
                except:
                    checkStr = checkStr[checkStr.index(s[i])]
              
            #Add currently checked character in string to the checkStr  
            checkStr += s[i]
            
            #If the current checkStr is larger than the stored substringLength, set substringLength to checkStr length
            if len(checkStr) > substringLength:
                substringLength = len(checkStr)       
        
        return substringLength