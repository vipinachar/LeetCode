def isPossible(answerKey, k, answer, n) -> bool:
    window_start = 0
    false_count = 0
    maxSum = 0
    for window_end in range(0, n):
        if answerKey[window_end] == "F":
            false_count += 1
            while false_count > k:
                removing_element = answerKey[window_start]
                if removing_element == "F":
                    false_count -= 1
                window_start += 1
        maxSum = max(maxSum, window_end - window_start + 1)

    if maxSum >= answer:
        return True

    window_start = 0
    true_count = 0
    maxSum = 0
    for window_end in range(0, n):
        if answerKey[window_end] == "T":
            true_count += 1
            while true_count > k:
                removing_element = answerKey[window_start]
                if removing_element == "T":
                    true_count -= 1
                window_start += 1
        maxSum = max(maxSum, window_end - window_start + 1)

    if maxSum >= answer:
        return True

    return False


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)

        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            if isPossible(answerKey, k, mid, n) == False:
                high = mid - 1
            else:
                if isPossible(answerKey, k, mid + 1, n) == False:
                    return mid
                else:
                    low = mid + 1
        return 1
