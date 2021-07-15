def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
     
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
             
        while array[end] > pivot:
            end -= 1
         
        if(start < end):
            array[start], array[end] = array[end], array[start]
     
    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    return end
     
def sort(array, start = None, end = None):
    if start == None and end == None:
        start = 0
        end = len(array) - 1
     
    if (start < end):
        p = partition(start, end, array)
         
        sort(array, start, p - 1)
        sort(array, p + 1, end)

    return array
