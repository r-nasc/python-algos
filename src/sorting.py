"""Simple sorting algorithms in Python"""
import random


def shell_sort(arr: list) -> list:
    """Sorts an array using the Shell sort algorithm.

    Time Complexity: O(n^3/2) avg and worst case. Memory: O(1)

    The method calculates a gap to be used (3x+1 in this example) and gap-sort
    the array. The gap is reduced until it reaches 1, which is the same as an
    insertion sort on a partially sorted array.
    """
    count = len(arr)
    gap = 1

    while gap < count // 3:
        gap = 3 * gap + 1

    while gap > 0:
        for i in range(gap, count):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3
    return arr


def insertion_sort(arr: list) -> list:
    """Sorts an array using the Insertion sort algorithm.

    Time complexity: O(n^2) avg and worst case. Memory: O(1)

    The method uses a for loop to iterate over each element in the list, starting
    from the second element (i==1). The while loop is used to iterate over the
    sorted list and find the correct position of the current element by shifting
    all greater elements to the right and inserting the current element after a
    smaller element is found.
    """
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr


def selection_sort(arr: list) -> list:
    """Sorts an array using the Selection sort algorithm.

    Time complexity: O(n^2) avg and worst case. Memory: O(1)

    The method uses a for loop to iterate over each element in the list. The
    inner for loop is used to find the smallest element in the unsorted part of
    the list and swap it with the first element of the unsorted part of the list.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def shuffle_sort(arr: list) -> list:
    """Sorts an array using the Shuffle sort algorithm.

    Time complexity: O(n) avg and worst case. Memory: O(1)

    The method uses a for loop to iterate over each element in the list and swap
    it with a random element in the list between the starting and current element.
    """
    for i in range(1, len(arr)):
        # pick an element in x[:i] with which to exchange x[i]
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def quick_sort(arr: list) -> list:
    """Sorts an array using the Quick sort algorithm.

    Time complexity: O(n log n) avg and O(n^2) worst case. Memory: O(log n)

    The method selects a pivot element from the array and partitions the other
    elements into two sub-arrays, according to whether they are less than or greater
    than the pivot. The sub-arrays are then recursively sorted.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


def merge_sort(arr: list) -> list:
    """Sorts an array using the Merge sort algorithm.

    Time complexity: O(n log n) avg and worst case. Memory: O(n)

    The method divides the array into two halves, sorts them recursively and then
    merges the two sorted halves. The merge operation is done by comparing the
    first element of each half and appending the smaller one to the result array.
    """

    def _combine(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _combine(left, right)


def heap_sort(arr: list) -> list:
    """Sorts an array using the Heap sort algorithm.

    Time complexity: O(n log n) avg and worst case. Memory: O(1)

    The method builds a max-heap from the array (heapify phase) and then swaps
    the first element of the array with the last element and rebuilds the heap
    (sortdown phase) until the array is sorted.
    """

    def _sink(k, n):
        """Sink the element at index k in the array of length n"""
        while 2 * k <= n:
            j = 2 * k
            if j < n and arr[j - 1] < arr[j]:
                j += 1
            if arr[k - 1] >= arr[j - 1]:
                break
            arr[k - 1], arr[j - 1] = arr[j - 1], arr[k - 1]
            k = j

    n = len(arr)

    # Heapify phase
    for k in range(n // 2, 0, -1):
        _sink(k, n)

    # Sortdown phase
    while n > 1:
        arr[0], arr[n - 1] = arr[n - 1], arr[0]
        n -= 1
        _sink(1, n)
