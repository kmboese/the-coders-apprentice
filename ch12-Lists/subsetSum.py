def subsetSum(numbers, start=0, mid=None, end=None, solutions=[]):
    if not mid and not end:
        mid = start+1
        end = len(numbers)-1

    if not numbers or start == mid or mid == end or \
    mid >= len(numbers) or start >= len(numbers) or end >= len(numbers)\
    or mid == end: 
        return solutions
    
    print("DEBUG: numbers = {}".format(numbers))

    if sum(numbers) == 0:
        solutions.append(numbers)

    # Recursive call
    # Test input: [1,4,-3,-5,7]
    subsetSum([numbers[start]] + numbers[mid:end] + [numbers[end]], start+1, mid, end)
    subsetSum([numbers[start]] + numbers[mid:end] + [numbers[end]], start, mid+1, end)
    subsetSum([numbers[start]] + numbers[mid:end] + [numbers[end]], start, mid, end-1)

    return solutions


'''
Input: [1,4,-3,-5,7]
[1,4,-3,-5,7] = 4
[1,-3,-5,7] = 0 --> return set
[1,-5,7] = 3
[1,7] = 8
[1] = 1
[] --> return
[1,4,-5,7] = 7
[1,-5,7] = 3
[1,-3] =-2
[1] = 1
[] --> return
[1,-3,-5,7] = 0 --> return set (duplicate work)
[1,-5,7] = 3
[1,7] = 8
[1] = 1
[] --> return
[1,-5,7] = 3
[1,7] = 8
[1] = 1
[] --> return
[1,7] = 8
[1] = 1
[] --> return
[1] = 1
[] --> return
'''