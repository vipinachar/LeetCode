class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for i in range(0,len(words)):
            word = words[i]

            if len(word) == 0:
                continue 

            start = 0 
            end = len(word) - 1 

            while start < end:
                if word[start] == word[end]:
                    start += 1 
                    end -= 1 
                else:
                    break 
                
            if start == end or start > end : 
                return word 
        
        return ""

        