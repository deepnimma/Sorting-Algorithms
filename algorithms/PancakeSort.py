def flip(arr, i):
    start = 0

    while start < i:
        arr[start], arr[i] = arr[i], arr[start]

        start += 1
        i -= 1

def findMax(arr, n):
    mi = 0

    for i in range(0, n):
        if arr[i] > arr[mi]:
            mi = i
    return mi

def sort(a, n = ''):
    if n == '':
        n = len(a)

    curr_size = n
    modarr = a

    while curr_size > 1:
        mi = findMax(modarr, curr_size)

        if mi != curr_size - 1:
            flip(modarr, mi)
            flip(modarr, curr_size - 1)

        curr_size -= 1

    return modarr