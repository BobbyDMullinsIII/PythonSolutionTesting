


class Problem7:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem7():
        #Main variables
        x = 123

        #Execute solution
        reversedNumber = Problem7.reverseSimple(x); #Simpler solution
        #reversedNumber = Problem7.reverseFasterSmaller(x) #Slightly faster and more space efficient solution

        #Solution printed out to console
        print(reversedNumber)
        
        
    def reverseSimple(x: int) -> int:
        strNum = str(x)
        
        #Remove negative sign for time being if number is negative
        if x < 0:
            strNum = strNum[1:]
            
        strNum = strNum[::-1] #Reverse string number
        
        #Add negative sign back if x is negative
        if x < 0:
            strNum = "-" + strNum
           
        #Returns int from string if no underflow or overflow occurred
        try:
            tempInt = int(strNum)
            
            if tempInt > 2147483647 or tempInt < -2147483648:
                return 0
            else:
                return tempInt
            
        except:
             return 0 #Returns 0 if error occurred
            
        
    def reverseFasterSmaller(x: int) -> int:
        strNum = str(x)
        
        #If x is a positive number
        if x >= 0:
            strNum = strNum[::-1] 
           
        #If x is a negative number
        else:
            strNum = strNum[1:]
            strNum = strNum[::-1]
            strNum = "-" + strNum
            
        #Returns int from string if no underflow or overflow occurred
        try:
            tempInt = int(strNum)
            
            if tempInt > 2147483647 or tempInt < -2147483648:
                return 0
            else:
                return tempInt
            
        except:
             return 0 #Returns 0 if error occurred