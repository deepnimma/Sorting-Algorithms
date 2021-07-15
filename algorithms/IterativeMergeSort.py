def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []

    i = j = 0

    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result

def sort(arg: list):
    if len(arg) < 2:
        return arg

    middle = int(len(arg) / 2)
    left = sort(arg[:middle])
    right = sort(arg[middle:])

    return merge(left, right)
        
if __name__ == '__main__':
    print(sort([1, 7, 6, 5, 8, 3, 10, 2, 9, 4]))