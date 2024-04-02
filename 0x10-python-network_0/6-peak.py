#!/usr/bin/python3
def find_peak(list_of_integers):
    """Finds a peak in the given list of unsorted integers.

    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        The value of a peak in the list, or None if no peak is found.
    """
    if (not list_of_integers):
        return None
    if (len(list_of_integers) <= 2):
        return max(list_of_integers)
    peak = None
    if (list_of_integers[0] >= list_of_integers[1]):
        peak = list_of_integers[0]
    if (list_of_integers[-1] >= list_of_integers[-2]):
        peak = list_of_integers[-1]
    if (peak):
        return peak
    idx = 1
    while (idx < len(list_of_integers) - 1):
        if (list_of_integers[idx] >= list_of_integers[idx + 1] and
                list_of_integers[idx] >= list_of_integers[idx - 1]):
            return list_of_integers[idx]
        else:
            idx += 1
    return peak
