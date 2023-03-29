


class Problem13:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem13():
        #Main variables
        s = "MCMXCIV"

        #Execute Solution
        convertInt = Problem13.romanToInt(s)

        #Solution printed out to console
        print(convertInt)
        
    def romanToInt(s: str) -> int:
        finalInt = 0 #Final converted integer to return
        
        #Dictionary of symbols and values for roman numeral to integer conversion
        symVals = {"I" : 1,
                   "IV" : 4,
                   "V" : 5,
                   "IX" : 9,
                   "X" : 10,
                   "XL" : 40,
                   "L" : 50,
                   "XC" : 90,
                   "C" : 100,
                   "CD" : 400,
                   "D" : 500,
                   "CM" : 900,
                   "M" : 1000}
        
        #Have to replace these because "edge" cases will not convert correctly without a lot of calculation
        #This makes it simpler
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")
        
        #Go through each value within the string and convert into integer representation
        for i in range(len(s)):
            finalInt += symVals[s[i]]
        
        #Return final converted number
        return finalInt