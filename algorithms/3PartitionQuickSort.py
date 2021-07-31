def sort(arr, left = 0, right = 0):
    right = right or len(arr) - 1
    modarr = arr

    if right <= left:
        return modarr

    a = i = left
    b = right
    pivot = modarr[left]

    while i <= b:
        if modarr[i] < pivot:
            modarr[a], modarr[i] = modarr[i], modarr[a]
            a += 1
            i += 1
        elif modarr[i] > pivot:
            modarr[b], modarr[i] = modarr[i], modarr[b]
            b -= 1
        else:
            i += 1

    sort(modarr, left, a - 1)
    sort(modarr, b + 1, right)

    return modarr
