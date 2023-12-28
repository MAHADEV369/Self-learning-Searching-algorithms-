def ExponentialSearch(numbers, val):
    if numbers[0] == val:
        return 0
    index = 1
    while index < len(numbers) and numbers[index] <= val:
        index = index * 2
    return BinarySearch( arr[:min(index, len(numbers))], val)

#worst time complexity O(logn)
