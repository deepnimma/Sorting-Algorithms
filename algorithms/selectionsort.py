import sys

def sort(arg: list):
    modarg = arg

    for i in range(len(modarg)):
        min_idx = i

        for j in range(i + 1, len(modarg)):
            if modarg[min_idx] > modarg[j]:
                min_idx = j

        modarg[i], modarg[min_idx] = modarg[min_idx], modarg[i]

    return modarg