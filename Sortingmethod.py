def Selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
# Taking the input From The Below
arr = list(map(int, input("Enter the elements of array : ").split()))
print("Sorted array is : ", Selection_sort(arr))
# Selection Sort Algorithm