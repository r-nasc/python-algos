"""Unit testing for sorting algorithms"""
import pytest
from src.sorting import (
    shell_sort,
    insertion_sort,
    selection_sort,
    merge_sort,
    quick_sort,
)


expected_values = [
    # Test empty list
    ([], []),
    # Test list with one element
    ([1], [1]),
    # Test list with two elements
    ([2, 1], [1, 2]),
    # Test list with multiple elements
    ([5, 3, 8, 4, 2], [2, 3, 4, 5, 8]),
    # Test list with duplicate elements
    ([5, 3, 8, 4, 2, 5, 3, 8, 4, 2], [2, 2, 3, 3, 4, 4, 5, 5, 8, 8]),
    # Test list with negative elements
    ([-5, -3, -8, -4, -2], [-8, -5, -4, -3, -2]),
    # Test list with mixed positive and negative elements
    ([5, -3, 8, -4, 2], [-4, -3, 2, 5, 8]),
    # Test list with floating point elements
    ([5.5, 3.3, 8.8, 4.4, 2.2], [2.2, 3.3, 4.4, 5.5, 8.8]),
    # Test list with string elements
    (["a", "b", "c"], ["a", "b", "c"]),
    # Test sorted list
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
]


@pytest.mark.parametrize("test_input,expected", expected_values)
def test_shell_sort(test_input, expected):
    """shell_sort unit testing"""
    assert shell_sort(test_input) == expected


@pytest.mark.parametrize("test_input,expected", expected_values)
def test_insertion_sort(test_input, expected):
    """insertion_sort unit testing"""
    assert insertion_sort(test_input) == expected


@pytest.mark.parametrize("test_input,expected", expected_values)
def test_selection_sort(test_input, expected):
    """selection_sort unit testing"""
    assert selection_sort(test_input) == expected


@pytest.mark.parametrize("test_input,expected", expected_values)
def test_quick_sort(test_input, expected):
    """quick_sort unit testing"""
    assert quick_sort(test_input) == expected


@pytest.mark.parametrize("test_input,expected", expected_values)
def test_merge_sort(test_input, expected):
    """merge_sort unit testing"""
    assert merge_sort(test_input) == expected
