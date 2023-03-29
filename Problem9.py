


class Problem9:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def runProblem9():
        #Main variables
        x = 121

        #Execute solution
        isPalindrome = Problem9.isPalindrome(x)

        #Solution printed out to console
        print(isPalindrome)
        
        
    def isPalindrome(x: int) -> bool:
        #Variables
        n = x
        tempNum = 0
        finalNum  = 0
         
        #Will loop until 'n' equals zero after going through each "digit" in 'x'
        while n > 0:
            tempNum = n % 10
            finalNum = (finalNum * 10) + tempNum
            n //= 10 #Go down to next "digit" in 'x' number for next loop
             
        #If the final looped number is equal to the initial 'x' integer, 'x' is a palindrome
        if finalNum == x:
            return True
        #Else 'x' is not a palindrome
        else:
            return False