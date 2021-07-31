from typing import List

def sort(arr):
    modarr = arr

    most_bits = max(len(bin(x)[2:]) for x in modarr)
    return _msd_radix_sort(modarr, most_bits)

def _msd_radix_sort(arr, bitpos):
    if bitpos == 0 or len(arr) in [0, 1]:
        return arr

    zeros = list()
    ones = list()

    for number in arr:
        if(number >> (bitpos - 1)) & 1:
            ones.append(number)
        else:
            zeros.append(number)

    zeros = _msd_radix_sort(zeros, bitpos - 1)
    ones = _msd_radix_sort(ones, bitpos - 1)

    # recombine lists
    res = zeros
    res.extend(ones)

    return res

# def msd_radix_sort_inplace(arr):

if __name__ == '__main__':
    print(sort([3, 2, 1, 5, 3, 6, 7]))
