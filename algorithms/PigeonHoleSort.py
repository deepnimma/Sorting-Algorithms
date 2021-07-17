def sort(arr):
    modarr = arr
    minv = min(modarr)
    maxv = max(modarr)

    size = maxv - minv + 1

    holes = [0] * size

    for x in modarr:
        holes[x - minv] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            modarr[i] = count + minv
            i += 1

    return modarr