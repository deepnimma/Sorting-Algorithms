def sort(arr):
    modarr = arr
    for i, _ in enumerate(modarr):
        print(i % 2 == 1)
        print(modarr[i - 1] > modarr[i])
        print('\n')
        if (i % 2 == 1) is (modarr[i - 1] > modarr[i]):
            modarr[i - 1], modarr[i] = modarr[i], modarr[i - 1]

    return modarr

if __name__ == '__main__':
    print(sort([1, 2, 3, 4, 5]))