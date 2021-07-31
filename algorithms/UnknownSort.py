def sort(arr):
    start, end = [], []

    while len(arr) > 1:
        minv, maxv = min(arr), max(arr)
        start.append(minv)
        end.append(maxv)
        arr.remove(minv)
        arr.remove(maxv)
    end.reverse()
    return start + arr + end

