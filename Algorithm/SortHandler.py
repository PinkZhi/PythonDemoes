class SortHandler:
    def __init__(self):
        return
    
    def _Partion2(self, array, left, right, compareFunc):
        povit = left

        """
        以最右边的数为比较值，将符合比较条件的数移到左边
        """
        for j in range(left, right):
            if compareFunc(array[j], array[right]):
                array[povit], array[j] = array[j], array[povit]
                povit += 1

        """
        最后将比较值放到povit位置上
        """    
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

        """
        将最左边的数作为比较值，将大于比较值的数放一边，等于比较值的数放中间，小于比较值的数放另一边
        """
        while i < gt:
            ret = compareFunc(array[i], povitValue)
            if 0 == ret:
                i += 1
            elif ret > 0:
                """
                和右边的数交换后，因为右边的数不知道和比较值的大小，需要重新比较一次，所以不需要 i++
                """
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