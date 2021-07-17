def sort(array):
    modarr = array

    writes = 0

    for cycleStart in range(0, len(modarr) - 1):
        item = modarr[cycleStart]

        pos = cycleStart
        for i in range(cycleStart + 1, len(modarr)):
            if modarr[i] < item:
                pos += 1

        if pos == cycleStart:
            continue

        while item == modarr[pos]:
            pos += 1
        modarr[pos], item = item, modarr[pos]
        writes += 1

        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(modarr)):
                if modarr[i] < item:
                    pos += 1

            while item == modarr[pos]:
                pos += 1

            modarr[pos], item = item, modarr[pos]

            writes += 1

    return modarr