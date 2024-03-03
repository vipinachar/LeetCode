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

        for i in range(2,n-1):
            baseRepresentation = getBaseRepresentation(n,i)
            if checkPallindrome(baseRepresentation) == False :
                return False 
        
        return True 
                


        