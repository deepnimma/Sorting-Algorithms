def countingsort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = arr[i] / exp1
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1
    i = 0

    arr = output

def sort(arr):
    try:
        max1 = max(arr)

        exp = 1
        while max1 / exp > 0:
            countingsort(arr, exp)
            exp *= 10
        
        return arr
    except:
        return arr