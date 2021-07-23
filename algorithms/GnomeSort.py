def sort(arr, n=''):
    if n == '':
        n = len(arr)

    modarr = arr

    i = 0

    while i < n:
        if i == 0:
            i += 1
        if modarr[i] >= modarr[i - 1]:
            i = i + 1
        else:
            modarr[i], modarr[i - 1] = modarr[i - 1], modarr[i]
            i -= 1

    return modarr
        