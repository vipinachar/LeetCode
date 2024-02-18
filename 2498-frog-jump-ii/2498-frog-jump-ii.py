class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 2:
            return stones[1]-stones[0]

        maxLength = float("-inf")
        for i in range(2,n,2):
            maxLength = max(maxLength, abs(stones[i]-stones[i-2]))

        if n%2!=0:
            starting_index=n-2
        else:
            starting_index=n-1
        for i in range(starting_index, 2,-2):
            maxLength = max(maxLength, abs(stones[i]-stones[i-2]))


                
        return maxLength
            

        