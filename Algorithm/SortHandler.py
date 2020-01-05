class SortHandler:
    def __init__(self):
        return
    
    def _Partion2(self, array, left, right, compareFunc):
        povit = left
        for j in range(left, right):
            if compareFunc(array[j], array[right]):
                array[povit], array[j] = array[j], array[povit]
                povit += 1
            
        array[povit], array[right] = array[right], array[povit]
        return povit

    def _QuickSort2(self, array, begin, end, compareFunc):
        if begin >= end:
            return
        
        divIndex = self._Partion2(array, begin, end, compareFunc)
        self._QuickSort2(array, begin, divIndex - 1, compareFunc)
        self._QuickSort2(array, divIndex + 1, end, compareFunc)
        return

    def QuickSort2(self, array, compareFunc):
        self._QuickSort2(array, 0, len(array) - 1, compareFunc)
        return