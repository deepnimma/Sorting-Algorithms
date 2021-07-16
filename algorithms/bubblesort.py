def sort(arg: list):
    n = len(arg)
    modarg = arg


    for i in range(n):
        for j in range(0, n - i - 1):
            if modarg[j] > modarg[j + 1]:
                modarg[j], modarg[j + 1] = modarg[j + 1], modarg[j]
    return modarg