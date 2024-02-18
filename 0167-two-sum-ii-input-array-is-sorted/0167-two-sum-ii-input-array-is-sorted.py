def BS(numbers: List[int], n: int, key: int) -> int:
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] > key:
            high = mid - 1
        else:
            if numbers[mid] == key and mid == n - 1:
                return n - 1
            elif numbers[mid] == key and numbers[mid + 1] != key:
                return mid
            else:
                low = mid + 1
    return -1


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(0, n):  # O(N)
            number1 = numbers[i]
            number1_index = i
            number2 = target - numbers[i]
            number2_index = BS(numbers, n, number2)  # O(logN)
            if number2_index != -1 and number1_index != number2_index:
                return [number1_index + 1, number2_index + 1]

        # O(NlogN)
