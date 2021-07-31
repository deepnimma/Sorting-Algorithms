# Only Making This Function Until I Can Figure Out What's Breaking This
def checksort(arr) -> bool:
    for i in range(len(arr) - 1):
        if (arr[i] > arr[i + 1]):
            return False

    return True

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

if __name__ == '__main__':
    print(sort([1, 5, 2, 6, 8, 3, 4]))

