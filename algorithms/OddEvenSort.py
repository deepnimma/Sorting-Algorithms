def sort(arr):
    modarr = arr

    didsort = False

    while not didsort:
        didsort = True

        for i in range(0, len(modarr) - 1, 2):
            if modarr[i] > modarr[i + 1]:
                modarr[i], modarr[i + 1] = modarr[i + 1], modarr[i]
                didsort = False
        
        for i in range(1, len(modarr) - 1, 2):
            if modarr[i] > modarr[i + 1]:
                modarr[i], modarr[i + 1] = modarr[i + 1], modarr[i]
                didsort = False

    return modarr