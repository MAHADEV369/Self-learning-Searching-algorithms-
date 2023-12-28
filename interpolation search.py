def InterpolationSearch(numbers, val):
    low = 0
    high = (len(numbers) - 1)
    while low <= high and val >= numbers[low] and val <= numbers[high]:
        index = low + int(((float(high - low) / ( numbers[high] - numbers[low])) * ( val - numbers[low])))
        if numbers[index] == val:
            return index
        if numbers[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1

#timecomplexity O(log log n)