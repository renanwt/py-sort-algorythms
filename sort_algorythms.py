# Quick Sort
# A Pivot Element is chosen inside a list
# A QuickSort is useful when TIME complexity MATTERS. This is because QuickSort use LESS MEMORY space than other
# algorithms, which gives them an efficiency boost. You should only use a QuickSort if you are familiar with Python
# recursion. This is because the QuickSort algorithm depends on recursive functions.

def quicksort(list, start=0, end=None):
    if end is None:
        end = len(list)-1
    if start < end:
        p = partition(list, start, end)
        quicksort(list, start, p-1)
        quicksort(list, p+1, end)


# to move pivot to center of the list and separate lower and higher values
def partition(list, start, end):
    pivot = list[end]
    s = start
    for j in range(start, end):
        if list[j] <= pivot:
            list[j], list[s] = list[s], list[j]
            s = s + 1
    list[s], list[end] = list[end], list[s]
    return s


# The biggest advantage of Merge sort is that it can sort LARGE DATA SETS easily because it has FASTER TIME complexity.
# It is also a stable sorting algorithm which means it maintains the relative order of equal elements. Also, merge sort
# works when sorting linked lists because of its divide-and-conquer approach.

def mergesort(list, start=0, end=None):
    if end is None:
        end = len(list)
    if end - start > 1:
        middle = (end + start)//2
        mergesort(list, start, middle)
        mergesort(list, middle, end)
        merge(list, start, middle, end)


def merge(list, start, middle, end):
    left = list[start:middle]
    right = list[middle:end]
    first_l, first_r = 0, 0
    for k in range(start, end):
        if first_l >= len(left):
            list[k] = right[first_r]
            first_r = first_r + 1
        elif first_r >= len(right):
            list[k] = left[first_l]
            first_l = first_l + 1
        elif left[first_l] < right[first_r]:
            list[k] = left[first_l]
            first_l += 1
        else:
            list[k] = right[first_r]
            first_r += 1
