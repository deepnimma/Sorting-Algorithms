def comp_and_swap(array, i, j, direction):
    if (direction == 1 and array[i] > array[j]) or (
        direction == 0 and array[i] < array[j]
    ):
        array[i], array[j] = array[j], array[i]


def bitonic_merge(array, low, length, direction):
    if length > 1:
        middle = int(length / 2)
        for i in range(low, low + middle):
            comp_and_swap(array, i, i + middle, direction)
        bitonic_merge(array, low, middle, direction)
        bitonic_merge(array, low + middle, middle, direction)


def sort(array, low = None, length = None, direction = None):
    if low == length == direction == None:
        low = 0
        length = len(array)
        direction = 1

    if length > 1:
        middle = int(length / 2)
        sort(array, low, middle, 1)
        sort(array, low + middle, middle, 0)
        bitonic_merge(array, low, length, direction)

    return array