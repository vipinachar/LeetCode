def getBaseRepresentation(n:int, i:int):
    answer = "" 
    while n > 0:
        remainder = n%i 
        answer += str(remainder)
        n = n//2
    answer += str(n)
    return answer

def checkPallindrome(value):
    start = 0 
    end = len(value)-1
    while start < end:
        if value[start] != value[end]:
            return False 
        start += 1
        end -= 1
    return True 

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        # i) brute force 

        for i in range(n-2,1,-1): # o(N)
            baseRepresentation = getBaseRepresentation(n,i) # o(logN)
            if checkPallindrome(baseRepresentation) == False : # o(N)
                return False 
        
        return True # o(n^2) sc o(1)
                


        