numbers = [38, 27, 43, 3, 9, 82, 10]

def merge(arr:list, left:int, right:int):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr:list)->list:
    n = len(arr)
    if n <= 1:
        return
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(arr, left, right)
    return arr

print(numbers) # [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(numbers)) # [3, 9, 10, 27, 38, 43, 82]