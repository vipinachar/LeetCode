class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        low = 0 
        high = n - 1
        while low<=high:
            mid=(low+high)//2 
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid 
            elif arr[mid] > arr[mid+1] and arr[mid] < arr[mid-1]:
                high = mid -1 
            else:
                low = mid + 1 
        return -1 
        
        