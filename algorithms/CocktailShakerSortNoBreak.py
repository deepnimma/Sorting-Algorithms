def sort(arr):
    modarr = arr

    for i in range(len(modarr) - 1, 0, -1):
        for j in range(i, 0, -1):
            if modarr[j] < modarr[j - 1]:
                modarr[j], modarr[j - 1] = modarr[j - 1], modarr[j]
        for j in range(i):
            if modarr[j] > modarr[j + 1]:
                modarr[j], modarr[j + 1] = modarr[j + 1], modarr[j]
    return modarr
