"""Simple sorting algorithms in Python"""
import random


def shell_sort(arr: list) -> list:
    """Sorts an array using the Shell sort algorithm."""
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
    """Sorts an array using the Insertion sort algorithm."""
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr


def selection_sort(arr: list) -> list:
    """Sorts an array using the Selection sort algorithm."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def shuffle_sort(arr: list) -> list:
    """Sorts an array using the Shuffle sort algorithm."""
    for i in range(1, len(arr)):
        # pick an element in x[:i] with which to exchange x[i]
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
