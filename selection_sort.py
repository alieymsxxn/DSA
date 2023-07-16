def selection_sort(arr=[12, 45, 67, 1, 34, 455, -10, 343, 2]):
    index = 0
    while index <= len(arr) - 2:
        _index = index
        mindex = _index
        while _index <= len(arr) - 1:
            if arr[mindex] > arr[_index]:
                mindex = _index
            _index = _index + 1
        temp = arr[index]
        arr[index] = arr[mindex]
        arr[mindex] = temp
        index = index + 1
    print(arr)
selection_sort()
