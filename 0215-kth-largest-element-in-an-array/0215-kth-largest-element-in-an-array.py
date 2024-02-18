def countNumbersLessThanOrEqual(nums, k, answer, n):
    count_of_numbers_less_than_equal = 0 
    for i in range(0,n):
        if nums[i] <= answer:
            count_of_numbers_less_than_equal += 1 
    
    return count_of_numbers_less_than_equal

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n =len(nums)
        low = float("inf")
        for i in range(0,n):
            if nums[i] < low:
                low = nums[i]
        
        high = float("-inf")
        for i in range(0,n):
            if nums[i] > high:
                high = nums[i] 
        
      
        while low<=high:
            mid=(low+high)//2
            if countNumbersLessThanOrEqual(nums,k,mid,n) < n-k+1:
                low = mid + 1 
            else:
                if countNumbersLessThanOrEqual(nums,k,mid-1,n) < n-k+1:
                    return mid 
                else:
                    high = mid -1 
        return 1

