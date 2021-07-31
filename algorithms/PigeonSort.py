from typing import List

def sort(arr):
    modarr = arr

    n = len(modarr)

    if n == 0:
        return modarr

    minv, maxv = min(modarr), max(modarr)

    holes_range = maxv - minv + 1
    holes, holesrepeat = [0] * holes_range, [0] * holes_range

    for i in modarr:
        index = i - minv
        holes[index] = i
        holesrepeat[index] += 1

    index = 0

    for i in range(holes_range):
        while holesrepeat[i] > 0:
            modarr[index] = holes[i]
            index += 1
            holesrepeat[i] -= 1

    return modarr