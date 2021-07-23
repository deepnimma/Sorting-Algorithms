def binsearch(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2

    if arr[mid] < val:
        return binsearch(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binsearch(arr, val, start, mid - 1)
    else:
        return mid


def sort(arr):
    modarr = arr

    for i in range(1, len(modarr)):
        val = modarr[i]
        j = binsearch(modarr, val, 0, i - 1)
        modarr = modarr[:j] + [val] + modarr[j:i] + modarr[i + 1:]

        # print(modarr)

    return modarr

if __name__ == '__main__':
    print(sort([37, 23, 0, 31, 22, 17, 12, 72, 31, 46, 100, 88, 54]))