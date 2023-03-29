


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
        #If string is 'None', only has one character, or the rows is equal to 1, return itself
        if s == None or s == "" or len(s) == 0 or len(s) == 1 or numRows == 1:
            return s
        
        #Variables
        indexStr = 0
        indexRow = 0
        nextRow = True
        charArray = ""
        
        #Set character array to string length and loop through each string character for each iteration
        charArray = charArray.ljust(len(s)) 
        for i in range (len(s)):
            tempList = list(charArray)
            tempList[i] = s[indexStr]
            charArray = ''.join(tempList)
            
            #Stay on current row if nextRow is false
            if nextRow == False:
                indexStr += (indexRow * 2)
            #Add number of rows 'numRows' to calculation if nextRow is true
            else:
                indexStr += (numRows - indexRow - 1) * 2
                
            #Invert 'nextRow' if 'indexRow' pointer is not zero
            if indexRow != 0:
                nextRow = not nextRow
                
            #If 'indexStr' is larger than the actual length of 's'
            #Go to top row by setting 'nextRow' to true and setting the pointers accordingly
            if indexStr >= len(s):
                indexRow += 1
                nextRow = True
                indexStr = indexRow
                
                #If the 'indexRow' pointer is equal to 1 below the number of rows in the zigzag conversion, reset it
                if indexRow == (numRows - 1):
                    indexRow = 0
        
        return charArray
                
            