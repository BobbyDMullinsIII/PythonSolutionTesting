


class Problem6:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem6():
        #Main variables
        s = "PAYPALISHIRING"
        numRows = 3

        #Execute solution
        converted = Problem6.convert(s, numRows)

        #Solution printed out to console
        print(converted)
        
        
    def convert(s: str, numRows: int) -> str:
        if s == None or s == "" or len(s) == 0 or len(s) == 1:
            return s
        
        indexStr = 0
        indexRow = 0
        nextRow = True
        charArray = ""
        charArray = charArray.ljust(len(s))
        
        for i in range (len(s)):
            tempList = list(charArray)
            tempList[i] = s[indexStr]
            charArray = ''.join(tempList)
            
            if nextRow == False:
                indexStr += (indexRow * 2)
            else:
                indexStr += (numRows - indexRow - 1) * 2
                
            if indexRow != 0:
                nextRow = not nextRow
                
            if indexStr >= len(s):
                indexRow += 1
                nextRow = True
                indexStr = indexRow
                
                if indexRow == (numRows - 1):
                    indexRow = 0
        
        return charArray
                
            