from SortHandle import _QuickSort2

def QuickSort_2_way(array, compareFunc):
    _QuickSort2(array, 0, len(array) - 1, compareFunc)
    return