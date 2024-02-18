def isPossible(position, m, n, k):
    ball_count = 1
    prev_ball_index = 0 
    for i in range(0, n):
        if abs(position[i]-position[prev_ball_index]) >= k:
            ball_count += 1
            prev_ball_index = i 
    
    if ball_count >= m:
        return True 

    return False 



class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n=len(position)
        low = 1
        high = position[n-1] 
        while low<=high:
            mid=(low+high)//2
            if isPossible(position, m, n, mid) == False:
                high = mid -1 
            else:
                if isPossible(position, m, n, mid+1) == False:
                    return mid 
                else:
                    low = mid + 1 
        return high  

        