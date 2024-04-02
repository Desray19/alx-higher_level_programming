#!/usr/bin/python3
def find_peak(list_of_integers):
    """Finds a peak in the given list of unsorted integers.

    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        The value of a peak in the list, or None if no peak is found.
    """

    length = len(list_of_integers)

    if length == 0:  # Handle empty list
        return None

    start = 0
    end = length - 1

    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:  # Look for a descending section
            end = mid
        else:  # Look for an ascending or flat section (potential peak)
            start = mid + 1

    return list_of_integers[start]  # The first element in the descending section is a peak

