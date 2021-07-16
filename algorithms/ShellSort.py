def sort(arr):
    gap = len(arr) // 2

    while gap > 0:
        i = 0
        j = gap

        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            
            j += 1
            i += 1

        while i - gap != -1:
            if arr[i - gap] > arr[i]:
                arr[i - gap], arr[i] = arr[i], arr[i - gap]
            i -= 1

        gap //= 2
    return arr
