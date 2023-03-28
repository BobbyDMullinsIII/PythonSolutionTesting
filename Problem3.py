


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
    
    @staticmethod
    def lengthOfLongestSubstring(s: str):
        checkStr = ""
        substringLength = -1
        
        if len(s.strip()) == 0 | len(s) == 0:
            return 0
        
        if len(s) == 0:
            return 1
        
        for i in range(len(s)):
            if s[i] in checkStr:
                try:
                    checkStr = checkStr[checkStr.index(s[i]) + 1]
                except:
                    checkStr = checkStr[checkStr.index(s[i])]
                
            checkStr += s[i]
            
            if len(checkStr) > substringLength:
                substringLength = len(checkStr)       
        
        return substringLength