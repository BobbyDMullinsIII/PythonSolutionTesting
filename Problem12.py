


from typing import List

class Problem12:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem12():
        #Main variables
        num = 3

        #Execute Solution
        romanNumeral = Problem12.intToRoman(num)

        #Solution printed out to console
        print(romanNumeral)
        
    def intToRoman(num: int) -> str:
        #Variables
        i = 12
        romanNumeral = ""
        
        #Dictionary of symbols and values for roman numeral to integer conversion
        valSyms = {1 : "I",
                   4 : "IV",
                   5 : "V",
                   9 : "IX",
                   10 : "X",
                   40 : "XL",
                   50 : "L",
                   90 : "XC",
                   100 : "C",
                   400 : "CD",
                   500 : "D",
                   900 : "CM",
                   1000 : "M"}
        
        while num > 0:
            tempNum = num // list(valSyms)[i]
            num %= list(valSyms)[i]

            while tempNum != 0:
                tempNum -= 1
                romanNumeral += list(valSyms.values())[i]
                
            i -=1
        
        #Return final converted roman numeral
        return romanNumeral