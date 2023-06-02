def findMissingRanges(nums, lower, upper):
    result = []
    start = lower
    
    for num in nums:
        if num > start:
            result.append(formatRange(start, num - 1))
        
        start = num + 1
    
    if start <= upper:
        result.append(formatRange(start, upper))
    
    return result


def formatRange(start, end):
    if start == end:
        return str(start)
    else:
        return [str(start),str(end)]
print(findMissingRanges([0,1,3,50,75],0,99))