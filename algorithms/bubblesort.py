def sort(arg: list):
    n = len(arg)
    modarg = arg

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if modarg[j] > modarg[j + 1]:
                modarg[j], modarg[j + 1] = modarg[j + 1], modarg[j]
                swapped = True

        if swapped == False:
            break

    return modarg

# print(bubblesort(['a', 'z', 'v', 'v', 'a', 'r', 'z', 'k', 's', 'j', 'g', 'u', 'h', 'm', 't', 'a', 'w', 'c', 'x', 'w', 'j', 's', 'i', 's', 'e', 'j']))
# print(bubblesort(['h', 'g', 'g', 'f', 'm', 'q', 'q', 'g', 'a', 'i', 'g', 'j', 'c', 'y', 'm', 'k', 'u', 'u', 'y', 't', 'x', 'q', 'f', 's', 'm', 'z']))