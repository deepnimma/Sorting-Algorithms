from typing import List

def sort(arr):
    modarr = arr
    n = len(modarr)

    if n == 0:
        return []

    minv, maxv = min(modarr), max(modarr)
    bucketcount = int(maxv - minv) + 1
    buckets: List[list] = [[] for _ in range(bucketcount)]

    for i in range(n):
        buckets[(int(modarr[i] - minv) // bucketcount)].append(modarr[i])

    return [v for bucket in buckets for v in sorted(bucket)]