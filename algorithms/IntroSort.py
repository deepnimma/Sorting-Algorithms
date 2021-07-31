import math

def insertion_sort(arr, start = 0, end = 0):
    end = end or len(arr)
    modarr = arr

    for i in range(start, end):
        temp_index = i
        temp = modarr[i]

        while temp_index != start and temp < modarr[temp_index - 1]:
            modarr[temp_index] = modarr[temp_index - 1]
            temp_index -= 1
        modarr[temp_index] = temp

    return modarr

def heapify(modarr, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and modarr[largest] < modarr[left_index]:
        largest = left_index

    if right_index < heap_size and modarr[largest] < modarr[right_index]:
        largest = right_index

    if largest != index:
        modarr[index], modarr[largest] = modarr[largest], modarr[index]
        heapify(modarr, largest, heap_size)

def sort(arr):
    modarr = arr
    n = len(modarr)

    if n < 16:
        return insertion_sort(modarr)

    for i in range(n // 2, -1, -1):
        heapify(modarr, i, n)
    
    for i in range(n - 1, 0, -1):
        modarr[i], modarr[0] = modarr[0], modarr[i]
        heapify(modarr, 0, i)

    return modarr