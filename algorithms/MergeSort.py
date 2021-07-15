def sort(arg: list):
    if len(arg) > 1:
        mid = len(arg) // 2

        L = arg[:mid]
        R = arg[mid:]

        sort(L)
        sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arg[k] = L[i]
                i += 1
            else:
                arg[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arg[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arg[k] = R[j]
            j += 1
            k += 1

        return arg