# CS2420 Quick Sort Example in Python

def quick_sort(arr):
    # Base case: if the array has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the middle element as the pivot
        pivot = arr[len(arr) // 2]
        # Elements less than the pivot go to the left
        left = [x for x in arr if x < pivot]
        # Elements equal to the pivot (handles duplicates)
        middle = [x for x in arr if x == pivot]
        # Elements greater than the pivot go to the right
        right = [x for x in arr if x > pivot]
        # Recursively sort left and right, then combine with middle
        return quick_sort(left) + middle + quick_sort(right)

unsorted_list = [3,6,8,10,1,2,1,44,23,12,78,90,33,22]
print("Unsorted List:", unsorted_list)
print("Sorted List:", quick_sort(unsorted_list))