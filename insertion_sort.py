def insertion_sort(arr):
    if len(arr) <= 1: return
    for i in range(1, len(arr)):
        k = arr[i]
        j = i-1
        while j >= 0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k

