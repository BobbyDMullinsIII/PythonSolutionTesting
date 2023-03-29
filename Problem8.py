


class Problem8:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem8():
        #Main variables
        s = "42"

        #Execute solution
        newInt = Problem8.myAtoi(s)

        #Solution printed out to console
        print(newInt)
        
    
    def myAtoi(s: str) -> int:
        pointer = 0
        numString = ""
        
        s = s.strip() #Remove all leading and trailing whitespace
        
        if len(s) == 0 or s == "":
            return 0
        
        #If both the first and second characters in the string are not a digit, return 0
        if(s[0].isdigit() == False):
            if len(s) == 1:
                return 0
            if s[1].isdigit() == False:
                return 0
            
            #If the first character is not a negative sign or positive sign, return 0
            if s[0] != '-' and s[0] != '+':
                return 0
            
        #Increments pointer forward if a plus or negative exists
        if s[pointer] == '-' or s[pointer] == '+':
            #Make 'numString' start with negative sign is in front of number if within 's'
            if s[pointer] == '-':
                numString += '-'

            pointer += 1; #Increment pointer to next position for digits
            
        #While the pointer is on a digit, add to the 'numString'
        while s[pointer].isdigit() == True:
            numString += s[pointer]
            pointer += 1

            if pointer == len(s):
                break
            
        #Check if number is valid and fits within sign 32-bit range
        #Clamp number if outside signed 32-bit range
        try:
            tempInt = int(numString)

            if tempInt < -2147483648:
                return -2147483648
            if tempInt > 2147483647:
                return 2147483647
            
            return numString
        
        except:
            #If negative, return min value, else return max value
            if numString[0] == '-':
                return -2147483648
            else:
                return 2147483647