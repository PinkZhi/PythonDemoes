def _QuickSortHelper2(array, left, right, compareFunc):
    povit = left
    for j in range(left, right):
        if compareFunc(array[j], array[right]):
            array[povit], array[j] = array[j], array[povit]
            povit += 1
    
    array[povit], array[right] = array[right], array[povit]
    return povit

def _QuickSort2(array, begin, end, compareFunc):
    if begin >= end:
        return

    divIndex = _QuickSortHelper2(array, begin, end, compareFunc)
    _QuickSort2(array, begin, divIndex - 1, compareFunc)
    _QuickSort2(array, divIndex + 1, end, compareFunc)
    return
    



