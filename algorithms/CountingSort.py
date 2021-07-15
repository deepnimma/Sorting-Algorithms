def sort(arr):
    try:
        maxelement = int(max(arr))
        minelement = int(min(arr))
    except:
        return stringsort(arr)
    rangeelements = maxelement - minelement + 1

    count_arr = [0 for _ in range(rangeelements)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(0, len(arr)):
        count_arr[arr[i] - minelement] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - minelement] - 1] = arr[i]
        count_arr[arr[i] - minelement] -= 1

    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

    return arr

def stringsort(arr):
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(256)]

    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]

    return ans