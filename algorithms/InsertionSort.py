def sort(arg: list):
    modarg = arg

    for i in range(1, len(modarg)):
        key = modarg[i]

        j = i - 1

        while j >= 0 and key < modarg[j]:
            modarg[j + 1] = modarg[j]
            j -= 1
        
        modarg[j + 1] = key

    return modarg

