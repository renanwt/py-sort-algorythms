# Quick Sort
# A Pivot Element is chosen inside a list
# A QuickSort is useful when time complexity matters. This is because QuickSort use less memory space than other
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


