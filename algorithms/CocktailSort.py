def sort(arr):
    modarr = arr

    n = len(modarr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped=False

        for i in range(start, end):
            if modarr[i] > modarr[i + 1]:
                modarr[i], modarr[i + 1] = modarr[i + 1], modarr[i]
                swapped = True

        if not swapped:
            break

        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if modarr[i] > modarr[i + 1]:
                modarr[i], modarr[i + 1] = modarr[i + 1], modarr[i]
                swapped = True

        start = start + 1

    return modarr