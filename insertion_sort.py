# Insertion Sort
# Takes an element and place it in its correct position
#TC -> worst - O(N^2)  best - O(N)
def insertion_sort(arr=[10, 4, 100,  12, 999, -999]):
    index = 0
    while index <= len(arr) - 1:
        _index = index
        while _index > 0 and arr[_index - 1] > arr[_index]:
            tmp = arr[_index - 1]
            arr[_index - 1] = arr[_index]
            arr[_index] = tmp
            _index = _index - 1
        index = index + 1
    print(arr)
insertion_sort()
