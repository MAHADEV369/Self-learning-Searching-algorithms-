import math

def JumpSearch (numbers, val):
    length = len(numbers)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and numbers[left] <= val:
        right = min(length - 1, left + jump)
        if numbers[left] <= val and numbers[right] >= val:
            break
        left += jump;
    if left >= length or numbers[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and numbers[i] <= val:
        if numbers[i] == val:
            return i
        i += 1
    return -1


#time complexity O(√n)