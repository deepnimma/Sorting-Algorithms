def sort(arr):
    modarg = arr
    try:
        maxelement = int(max(modarg))
        minelement = int(min(modarg))
    except:
        return stringsort(modarg)
    rangeelements = maxelement - minelement + 1

    count_arr = [0 for _ in range(rangeelements)]
    output_arr = [0 for _ in range(len(modarg))]

    for i in range(0, len(modarg)):
        count_arr[modarg[i] - minelement] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(modarg) - 1, -1, -1):
        output_arr[count_arr[modarg[i] - minelement] - 1] = modarg[i]
        count_arr[modarg[i] - minelement] -= 1

    for i in range(0, len(modarg)):
        modarg[i] = output_arr[i]

    return modarg