def sort(arr):
    modarr = arr

    for i in range(len(modarr) - 1, 0, -1):
        swapped = False

        for j in range(i, 0, -1):
            if modarr[j] < modarr[j - 1]:
                modarr[j], modarr[j - 1] = modarr[j - 1], modarr[j]
                swapped = True

        for j in range(i):
            if modarr[j] > modarr[j + 1]:
                modarr[j], modarr[j + 1] = modarr[j + 1], modarr[j]
                swapped = True

        if not swapped:
            break
    return modarr
