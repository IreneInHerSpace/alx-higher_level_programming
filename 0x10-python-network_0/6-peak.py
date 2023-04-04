#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers: A list of integers.

    Returns:
        The peak element in the list.

    Raises:
        ValueError: If the list is empty.
    """

    # Check for empty list
    if not list_of_integers:
        raise ValueError('List is empty')

    # Define start and end indices
    start, end = 0, len(list_of_integers) - 1

    # Binary search to find the peak
    while start < end:
        mid = (start + end) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return list_of_integers[start]
