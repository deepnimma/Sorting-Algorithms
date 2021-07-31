def sort(arr):
    modarr = arr
    cur = len(modarr)

    while cur > 1:
        mi = modarr.index(max(modarr[0:cur]))
        modarr = modarr[mi::-1] + modarr[mi + 1 : len(modarr)]
        modarr = modarr[cur - 1 :: -1] + modarr[cur : len(modarr)]
        cur -= 1
    
    return modarr