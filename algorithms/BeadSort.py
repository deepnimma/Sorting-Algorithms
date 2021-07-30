def sort(arr):
    for i in range(len(arr)):
        for i, (upper, lower) in enumerate(zip(arr, arr[1:])):
            if upper > lower:
                arr[i] -= upper - lower
                arr[i + 1] += upper - lower
    
    return arr