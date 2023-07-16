1. An outer loop runs from index n - 1 to 0.
2. The inner loops runs from 0 to (outer index) - 1
3. The logic inside inner loop will check if element at current index is greater than the element at next. If yes, they are swapped. It basically compares adjacent elements. 
4. With each iteration of outer loop the largest number is moved to the end of the array or subarray(focused by indexes)
5. The inner loop will run n - 2 times.
6. The outer loop will run n - 1 times.
7. The complexity of worst case scenario is O(n^2).
8. We can add a check that if a swap did not happen during a single inner loop iteration, it means our array is in ascending order. We can stop our execution here. 
9. The best case scenario is if our first iteration of inner loop swaps nothing, we break the outer loop as we know our array is sorted in ascending order.


def bubble_sort(arr=[1, 2, 3, 4, 5]):
    index = len(arr) - 1
    while index >= 0:
        _index = 0
        did_swap = False
        while _index <= index - 1:
            if arr[_index] > arr[_index + 1]:
                temp = arr[_index]
                arr[_index] = arr[_index + 1]
                arr[_index + 1] = temp
                did_swap = True
            _index = _index + 1
        if did_swap == False:
            break
        index = index - 1
    print(arr)
bubble_sort()
