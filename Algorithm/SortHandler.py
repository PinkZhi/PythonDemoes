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

    def _Partion3(self, array, begin, end, compareFunc):
        lt, i, gt = begin, begin + 1, end + 1
        povitValue = array[begin]

        while i < gt:
            ret = compareFunc(array[i], povitValue)
            if 0 == ret:
                i += 1
            elif ret > 0:
                array[gt - 1], array[i] = array[i], array[gt - 1]
                gt -= 1
            else:
                array[lt + 1], array[i] = array[i], array[lt + 1]
                lt += 1
                i += 1

        array[lt], array[begin] = array[begin], array[lt]

        return lt - 1, gt

    def _QuickSort3(self, array, begin, end, compareFunc):
        if begin >= end:
            return

        ltEnd, gtStart = self._Partion3(array, begin, end, compareFunc)
        self._QuickSort3(array, begin, ltEnd, compareFunc)
        self._QuickSort3(array, gtStart, end, compareFunc)
        return

    def QuickSort3(self, array, compareFunc):
        self._QuickSort3(array, 0, len(array) - 1, compareFunc)
        return